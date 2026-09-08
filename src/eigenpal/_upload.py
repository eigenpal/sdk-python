"""Client protocol for ``presigned-multipart`` file uploads."""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Optional

import httpx

MULTIPART_UPLOAD_CONCURRENCY = 4
MULTIPART_PART_MAX_RETRIES = 4
MULTIPART_PART_RETRY_BASE_MS = 250


def storage_upload_timeout(connect_seconds: float) -> httpx.Timeout:
    """Timeout for direct storage PUTs.

    Keep a connect/pool budget so an unreachable host fails quickly, but do
    not impose a read/write deadline — multi-GB parts routinely exceed the
    60s Eigenpal API timeout.
    """
    return httpx.Timeout(
        connect=connect_seconds,
        read=None,
        write=None,
        pool=connect_seconds,
    )


def expected_part_byte_length(
    total_size: int, part_size_bytes: int, part_number: int, part_count: int
) -> int:
    if part_number < 1 or part_number > part_count:
        raise ValueError(f"partNumber must be an integer in [1, {part_count}]")
    if total_size == 0:
        return 0
    if part_number < part_count:
        return part_size_bytes
    remainder = total_size % part_size_bytes
    return part_size_bytes if remainder == 0 else remainder


def part_byte_offset(part_size_bytes: int, part_number: int) -> int:
    return (part_number - 1) * part_size_bytes


def is_transient_http_status(status: int) -> bool:
    return status == 408 or status == 429 or 500 <= status <= 599


def part_is_authoritatively_complete(
    listed: list[dict[str, Any]], part_number: int, expected_size: int
) -> bool:
    found = next(
        (part for part in listed if part.get("partNumber") == part_number), None
    )
    if found is None:
        return False
    # Server complete rejects missing sizes. Treat them as incomplete so resume
    # re-uploads instead of skipping a part the API cannot finalize.
    return found.get("size") == expected_size


class PartUploadHttpError(Exception):
    def __init__(self, status: int) -> None:
        super().__init__(f"Storage part upload failed ({status})")
        self.status = status


def is_retryable_part_error(error: BaseException) -> bool:
    if isinstance(error, PartUploadHttpError):
        return is_transient_http_status(error.status)
    return isinstance(error, httpx.TransportError)


def should_abort_multipart_upload_session(*, parts_ready: bool) -> bool:
    """Abort leftover MPU state only while parts are not yet authoritative.

    After every expected part is listed, POST complete is idempotent.
    409/429/timeout/lost responses must not abort — that would delete GiB of
    uploaded parts and can race a complete that already succeeded server-side.
    Caller cancellation and unrecoverable part failures still abort because
    ``parts_ready`` is false in those cases.
    """
    return not parts_ready


def multipart_complete_retry_hint(upload_id: str) -> str:
    return (
        f"Uploaded parts remain stored for {upload_id}; "
        "retry complete and do not abort the session."
    )


def annotate_multipart_complete_failure(
    upload_id: str, error: BaseException
) -> BaseException:
    hint = multipart_complete_retry_hint(upload_id)
    if hint in str(error):
        return error
    try:
        error.args = (f"{error} {hint}",) + error.args[1:]
    except Exception:
        pass
    return error


def annotate_presigned_put_complete_failure(
    upload_id: str, error: BaseException
) -> BaseException:
    hint = (
        f"Uploaded file remains stored for {upload_id}; "
        "retry complete and do not abort the session."
    )
    if hint in str(error):
        return error
    try:
        error.args = (f"{error} {hint}",) + error.args[1:]
    except Exception:
        pass
    return error


def upload_presigned_multipart_parts(
    *,
    part_count: int,
    part_size_bytes: int,
    total_size: int,
    list_parts: Callable[[], list[dict[str, Any]]],
    presign_part: Callable[[int], dict[str, Any]],
    put_part: Callable[[str, dict[str, str], int, int], None],
    on_progress: Optional[Callable[[int, int], None]] = None,
    concurrency: int = MULTIPART_UPLOAD_CONCURRENCY,
) -> None:
    uploaded_bytes = 0
    credited: set[int] = set()

    def credit(part_number: int, length: int) -> None:
        nonlocal uploaded_bytes
        if part_number in credited:
            return
        credited.add(part_number)
        uploaded_bytes += length
        if on_progress is not None:
            on_progress(uploaded_bytes, total_size)

    def pending_part_numbers() -> list[int]:
        listed = list_parts()
        pending: list[int] = []
        for part_number in range(1, part_count + 1):
            length = expected_part_byte_length(
                total_size, part_size_bytes, part_number, part_count
            )
            if part_is_authoritatively_complete(listed, part_number, length):
                credit(part_number, length)
                continue
            pending.append(part_number)
        return pending

    def upload_one(part_number: int) -> None:
        length = expected_part_byte_length(
            total_size, part_size_bytes, part_number, part_count
        )
        start = part_byte_offset(part_size_bytes, part_number)
        last_error: Optional[BaseException] = None
        for attempt in range(MULTIPART_PART_MAX_RETRIES + 1):
            try:
                signed = presign_part(part_number)
                part_length = signed.get("partSizeBytes", length)
                headers = {
                    str(name): str(value)
                    for name, value in (signed.get("headers") or {}).items()
                }
                put_part(signed["url"], headers, start, part_length)
                credit(part_number, length)
                return
            except Exception as error:
                last_error = error
                if (
                    not is_retryable_part_error(error)
                    or attempt == MULTIPART_PART_MAX_RETRIES
                ):
                    raise
                time.sleep((MULTIPART_PART_RETRY_BASE_MS * (2**attempt)) / 1000)
        if last_error is not None:
            raise last_error

    pending = pending_part_numbers()
    if pending:
        _run_pool(pending, concurrency, upload_one)
    pending = pending_part_numbers()
    if pending:
        _run_pool(pending, concurrency, upload_one)
        pending = pending_part_numbers()
    if pending:
        raise RuntimeError(
            f"Upload incomplete: {len(pending)} part(s) missing from storage before complete"
        )


def _run_pool(
    items: list[int], concurrency: int, worker: Callable[[int], None]
) -> None:
    if not items:
        return
    workers = min(max(1, concurrency), len(items))
    first_error: Optional[BaseException] = None
    pool = ThreadPoolExecutor(max_workers=workers)
    futures = [pool.submit(worker, item) for item in items]
    try:
        for future in as_completed(futures):
            error = future.exception()
            if error is None:
                continue
            if isinstance(error, KeyboardInterrupt):
                first_error = error
                for pending in futures:
                    pending.cancel()
                raise error
            if first_error is None:
                first_error = error
            for pending in futures:
                pending.cancel()
            break
    finally:
        if first_error is None:
            pool.shutdown(wait=True)
        else:
            pool.shutdown(wait=False, cancel_futures=True)
    if first_error is not None:
        raise first_error
