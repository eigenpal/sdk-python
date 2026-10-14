"""Client protocol for ``http-chunked`` file uploads.

Resume listing is omitted — a retry re-sends from chunk 0. The server
accepts idempotent overwrite of an already-staged index.
"""

from __future__ import annotations

from typing import Callable, Optional


def expected_http_chunk_byte_length(
    total_size: int, chunk_size_bytes: int, chunk_index: int, chunk_count: int
) -> int:
    if chunk_index < 0 or chunk_index >= chunk_count:
        raise ValueError(f"chunkIndex must be an integer in [0, {chunk_count})")
    if total_size == 0:
        return 0
    if chunk_index < chunk_count - 1:
        return chunk_size_bytes
    remainder = total_size % chunk_size_bytes
    return chunk_size_bytes if remainder == 0 else remainder


def chunk_byte_offset(chunk_size_bytes: int, chunk_index: int) -> int:
    return chunk_index * chunk_size_bytes


def should_abort_http_chunked_upload_session(*, chunks_ready: bool) -> bool:
    return not chunks_ready


def http_chunked_complete_retry_hint(upload_id: str) -> str:
    return (
        f"Uploaded chunks remain stored for {upload_id}; "
        "retry complete and do not abort the session."
    )


def annotate_http_chunked_complete_failure(
    upload_id: str, error: BaseException
) -> BaseException:
    hint = http_chunked_complete_retry_hint(upload_id)
    if hint in str(error):
        return error
    try:
        error.args = (f"{error} {hint}",) + error.args[1:]
    except Exception:
        pass
    return error


def upload_http_chunks(
    *,
    chunk_count: int,
    chunk_size_bytes: int,
    total_size: int,
    put_chunk: Callable[[int, int, int], None],
    on_progress: Optional[Callable[[int, int], None]] = None,
) -> None:
    uploaded_bytes = 0
    for chunk_index in range(chunk_count):
        length = expected_http_chunk_byte_length(
            total_size, chunk_size_bytes, chunk_index, chunk_count
        )
        start = chunk_byte_offset(chunk_size_bytes, chunk_index)
        put_chunk(chunk_index, start, length)
        uploaded_bytes += length
        if on_progress is not None:
            on_progress(uploaded_bytes, total_size)
