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
from pathlib import Path
from typing import IO, Any, Optional, Tuple


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
    if isinstance(value, Path):
        content = value.read_bytes()
        filename = value.name
        mime_type, _ = mimetypes.guess_type(filename)
        return (filename, content, mime_type or "application/octet-stream")

    if isinstance(value, dict):
        raw_content = value["content"]
        content = bytes(raw_content) if isinstance(raw_content, bytearray) else raw_content
        filename = value["filename"]
        mime_type = value.get("mime_type") or value.get("mimeType")
        if not mime_type:
            mime_type, _ = mimetypes.guess_type(filename)
        return (filename, content, mime_type or "application/octet-stream")

    # File-like object (open() handle, BytesIO, etc.).
    handle: IO[bytes] = value
    content = handle.read()
    name = getattr(handle, "name", None)
    if isinstance(name, str):
        # Strip directory prefix (e.g. "/tmp/foo.pdf" → "foo.pdf").
        filename = Path(name).name
    else:
        filename = "file"
    mime_type, _ = mimetypes.guess_type(filename)
    return (filename, content, mime_type or "application/octet-stream")
