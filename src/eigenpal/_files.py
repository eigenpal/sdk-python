"""File-input helpers for ``client.run()``.

The Eigenpal API accepts file inputs two ways: inline base64 in JSON, or
``multipart/form-data`` (the same shape as ``curl -F``). The SDK auto-detects
file values in ``input`` and uses **multipart** — no base64 round-trip,
no size penalty.

Supported file values
---------------------

- ``pathlib.Path``      — read from disk; filename + mime type inferred
- explicit ``dict``      — ``{"content": bytes, "filename": str, "mime_type": str?}``
- ``BinaryIO`` (e.g. ``open("file", "rb")``) with a ``.name`` attribute

For raw ``bytes`` without metadata, wrap them in the explicit dict shape —
the workflow processor needs the filename to forward downstream.
"""

from __future__ import annotations

import mimetypes
import os
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Any, Optional, Tuple

from eigenpal.errors import EigenpalError


def is_file_input(value: Any) -> bool:
    """Detect whether a value should be uploaded as multipart."""
    if isinstance(value, Path):
        return True
    if isinstance(value, dict):
        content = value.get("content")
        filename = value.get("filename")
        return isinstance(filename, str) and isinstance(content, (bytes, bytearray))
    # File-like (open(..., "rb")) — duck type on read + name.
    if hasattr(value, "read") and hasattr(value, "name"):
        return True
    return False


def has_file_input(input_dict: Optional[dict[str, Any]]) -> bool:
    if not input_dict:
        return False
    return any(is_file_input(v) for v in input_dict.values())


def to_upload_tuple(value: Any) -> Tuple[str, bytes, str]:
    """Coerce a file input into the ``(filename, content, mime_type)`` triple
    that ``httpx`` accepts for its ``files=`` parameter."""
    source = inspect_upload_source(value)
    if source.content is not None:
        return (source.filename, source.content, source.mime_type)
    return (source.filename, read_part(source, 0, source.size), source.mime_type)


@dataclass
class UploadSource:
    filename: str
    mime_type: str
    size: int
    replayable: bool
    content: Optional[bytes] = None
    path: Optional[str] = None
    handle: Optional[IO[bytes]] = None
    _lock: Optional[threading.Lock] = None


def inspect_upload_source(value: Any) -> UploadSource:
    """Inspect a file value without loading the whole object when possible."""
    if isinstance(value, Path):
        filename = value.name
        mime_type, _ = mimetypes.guess_type(filename)
        return UploadSource(
            filename=filename,
            mime_type=mime_type or "application/octet-stream",
            size=value.stat().st_size,
            replayable=True,
            path=str(value),
        )

    if isinstance(value, dict):
        raw_content = value["content"]
        content = bytes(raw_content) if isinstance(raw_content, bytearray) else raw_content
        if not isinstance(content, (bytes, bytearray)):
            raise EigenpalError(
                "File descriptors require bytes content, a path, or a seekable file object.",
                status=0,
            )
        filename = value["filename"]
        mime_type = value.get("mime_type") or value.get("mimeType")
        if not mime_type:
            mime_type, _ = mimetypes.guess_type(filename)
        return UploadSource(
            filename=filename,
            mime_type=mime_type or "application/octet-stream",
            size=len(content),
            replayable=True,
            content=bytes(content),
        )

    handle: IO[bytes] = value
    seekable = bool(getattr(handle, "seekable", lambda: False)())
    if not seekable:
        raise EigenpalError(
            "Cannot multipart-resume a non-seekable stream; pass a path or seekable file object.",
            status=0,
        )
    position = handle.tell()
    handle.seek(0, os.SEEK_END)
    size = handle.tell()
    handle.seek(position)
    name = getattr(handle, "name", None)
    if isinstance(name, str) and name not in {"", "<stdin>"}:
        filename = Path(name).name
        path = name if os.path.isfile(name) else None
    else:
        filename = "file"
        path = None
    mime_type, _ = mimetypes.guess_type(filename)
    return UploadSource(
        filename=filename,
        mime_type=mime_type or "application/octet-stream",
        size=size,
        replayable=True,
        path=path,
        handle=None if path else handle,
        _lock=None if path else threading.Lock(),
    )


def read_part(source: UploadSource, start: int, length: int) -> bytes:
    if length == 0:
        return b""
    if source.content is not None:
        return source.content[start : start + length]
    if source.path is not None:
        with open(source.path, "rb") as handle:
            handle.seek(start)
            data = handle.read(length)
        if len(data) != length:
            raise EigenpalError(
                f"Expected {length} bytes at offset {start}, read {len(data)}.",
                status=0,
            )
        return data
    if source.handle is None:
        raise EigenpalError("Upload source is missing readable bytes.", status=0)
    lock = source._lock or threading.Lock()
    with lock:
        source.handle.seek(start)
        data = source.handle.read(length)
    if len(data) != length:
        raise EigenpalError(
            f"Expected {length} bytes at offset {start}, read {len(data)}.",
            status=0,
        )
    return data
