from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
from typing import Literal, cast
import datetime

if TYPE_CHECKING:
  from ..models.presigned_file_upload_session_headers import PresignedFileUploadSessionHeaders





T = TypeVar("T", bound="PresignedFileUploadSession")



@_attrs_define
class PresignedFileUploadSession:
    """
        Attributes:
            transport (Literal['presigned-put']):
            upload_id (str):
            file_id (str):
            url (str):
            headers (PresignedFileUploadSessionHeaders):
            expires_at (datetime.datetime):
            max_file_size_bytes (int):
     """

    transport: Literal['presigned-put']
    upload_id: str
    file_id: str
    url: str
    headers: PresignedFileUploadSessionHeaders
    expires_at: datetime.datetime
    max_file_size_bytes: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.presigned_file_upload_session_headers import PresignedFileUploadSessionHeaders
        transport = self.transport

        upload_id = self.upload_id

        file_id = self.file_id

        url = self.url

        headers = self.headers.to_dict()

        expires_at = self.expires_at.isoformat()

        max_file_size_bytes = self.max_file_size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "uploadId": upload_id,
            "fileId": file_id,
            "url": url,
            "headers": headers,
            "expiresAt": expires_at,
            "maxFileSizeBytes": max_file_size_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.presigned_file_upload_session_headers import PresignedFileUploadSessionHeaders
        d = dict(src_dict)
        transport = cast(Literal['presigned-put'] , d.pop("transport"))
        if transport != 'presigned-put':
            raise ValueError(f"transport must match const 'presigned-put', got '{transport}'")

        upload_id = d.pop("uploadId")

        file_id = d.pop("fileId")

        url = d.pop("url")

        headers = PresignedFileUploadSessionHeaders.from_dict(d.pop("headers"))




        expires_at = isoparse(d.pop("expiresAt"))




        max_file_size_bytes = d.pop("maxFileSizeBytes")

        presigned_file_upload_session = cls(
            transport=transport,
            upload_id=upload_id,
            file_id=file_id,
            url=url,
            headers=headers,
            expires_at=expires_at,
            max_file_size_bytes=max_file_size_bytes,
        )

        return presigned_file_upload_session
