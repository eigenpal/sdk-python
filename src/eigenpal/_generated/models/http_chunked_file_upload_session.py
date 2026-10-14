from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast
import datetime






T = TypeVar("T", bound="HttpChunkedFileUploadSession")



@_attrs_define
class HttpChunkedFileUploadSession:
    """
        Attributes:
            transport (Literal['http-chunked']):
            upload_id (str):
            file_id (str):
            chunk_size_bytes (int):
            chunk_count (int):
            chunks_url (str):
            complete_url (str):
            expires_at (datetime.datetime):
            max_file_size_bytes (int):
     """

    transport: Literal['http-chunked']
    upload_id: str
    file_id: str
    chunk_size_bytes: int
    chunk_count: int
    chunks_url: str
    complete_url: str
    expires_at: datetime.datetime
    max_file_size_bytes: int





    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        upload_id = self.upload_id

        file_id = self.file_id

        chunk_size_bytes = self.chunk_size_bytes

        chunk_count = self.chunk_count

        chunks_url = self.chunks_url

        complete_url = self.complete_url

        expires_at = self.expires_at.isoformat()

        max_file_size_bytes = self.max_file_size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "uploadId": upload_id,
            "fileId": file_id,
            "chunkSizeBytes": chunk_size_bytes,
            "chunkCount": chunk_count,
            "chunksUrl": chunks_url,
            "completeUrl": complete_url,
            "expiresAt": expires_at,
            "maxFileSizeBytes": max_file_size_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transport = cast(Literal['http-chunked'] , d.pop("transport"))
        if transport != 'http-chunked':
            raise ValueError(f"transport must match const 'http-chunked', got '{transport}'")

        upload_id = d.pop("uploadId")

        file_id = d.pop("fileId")

        chunk_size_bytes = d.pop("chunkSizeBytes")

        chunk_count = d.pop("chunkCount")

        chunks_url = d.pop("chunksUrl")

        complete_url = d.pop("completeUrl")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        max_file_size_bytes = d.pop("maxFileSizeBytes")

        http_chunked_file_upload_session = cls(
            transport=transport,
            upload_id=upload_id,
            file_id=file_id,
            chunk_size_bytes=chunk_size_bytes,
            chunk_count=chunk_count,
            chunks_url=chunks_url,
            complete_url=complete_url,
            expires_at=expires_at,
            max_file_size_bytes=max_file_size_bytes,
        )

        return http_chunked_file_upload_session
