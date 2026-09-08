"""Unit tests for presigned-multipart upload retry and pool behavior."""

from __future__ import annotations

import threading
import time

import httpx
import pytest

from eigenpal._upload import (
    PartUploadHttpError,
    annotate_presigned_put_complete_failure,
    is_retryable_part_error,
    upload_presigned_multipart_parts,
)


def test_presigned_put_complete_failure_explains_safe_retry() -> None:
    error = RuntimeError("complete timed out")
    annotate_presigned_put_complete_failure("fup_test", error)

    assert "Uploaded file remains stored for fup_test" in str(error)
    assert "retry complete and do not abort" in str(error)


def test_is_retryable_part_error_only_transient_http_and_transport() -> None:
    assert is_retryable_part_error(PartUploadHttpError(503))
    assert is_retryable_part_error(PartUploadHttpError(429))
    assert not is_retryable_part_error(PartUploadHttpError(403))
    assert not is_retryable_part_error(PartUploadHttpError(400))
    assert is_retryable_part_error(httpx.ConnectError("connection refused"))
    assert not is_retryable_part_error(ValueError("bad input"))
    assert not is_retryable_part_error(RuntimeError("logic bug"))


def test_403_is_not_retried() -> None:
    attempts: list[int] = []

    def put_part(url: str, headers: dict[str, str], start: int, length: int) -> None:
        attempts.append(1)
        raise PartUploadHttpError(403)

    with pytest.raises(PartUploadHttpError) as exc_info:
        upload_presigned_multipart_parts(
            part_count=1,
            part_size_bytes=4,
            total_size=4,
            list_parts=lambda: [],
            presign_part=lambda part_number: {
                "url": "https://storage.example/part-1",
                "headers": {},
            },
            put_part=put_part,
        )

    assert exc_info.value.status == 403
    assert len(attempts) == 1


def test_keyboard_interrupt_is_not_retried_or_swallowed() -> None:
    attempts: list[int] = []

    def put_part(url: str, headers: dict[str, str], start: int, length: int) -> None:
        attempts.append(1)
        raise KeyboardInterrupt()

    with pytest.raises(KeyboardInterrupt):
        upload_presigned_multipart_parts(
            part_count=1,
            part_size_bytes=4,
            total_size=4,
            list_parts=lambda: [],
            presign_part=lambda part_number: {
                "url": "https://storage.example/part-1",
                "headers": {},
            },
            put_part=put_part,
        )

    assert len(attempts) == 1


def test_pool_stops_waiting_on_sibling_parts_after_hard_failure() -> None:
    started: list[int] = []
    finished: list[int] = []
    lock = threading.Lock()
    release = threading.Event()

    def put_part(url: str, headers: dict[str, str], start: int, length: int) -> None:
        part_number = int(url.rsplit("-", 1)[-1])
        with lock:
            started.append(part_number)
        if part_number == 1:
            raise PartUploadHttpError(403)
        release.wait(timeout=5)
        with lock:
            finished.append(part_number)

    started_at = time.monotonic()
    with pytest.raises(PartUploadHttpError) as exc_info:
        upload_presigned_multipart_parts(
            part_count=4,
            part_size_bytes=4,
            total_size=16,
            list_parts=lambda: [],
            presign_part=lambda part_number: {
                "url": f"https://storage.example/part-{part_number}",
                "headers": {},
                "partSizeBytes": 4,
            },
            put_part=put_part,
            concurrency=4,
        )
    elapsed = time.monotonic() - started_at

    assert exc_info.value.status == 403
    assert 1 in started
    assert finished == []
    assert elapsed < 1.0
