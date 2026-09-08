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
  from ..models.presign_file_upload_part_response_headers import PresignFileUploadPartResponseHeaders





T = TypeVar("T", bound="PresignFileUploadPartResponse")



@_attrs_define
class PresignFileUploadPartResponse:
    """
        Attributes:
            transport (Literal['presigned-multipart']):
            part_number (int):
            url (str):
            headers (PresignFileUploadPartResponseHeaders):
            expires_at (datetime.datetime):
            part_size_bytes (int):
     """

    transport: Literal['presigned-multipart']
    part_number: int
    url: str
    headers: PresignFileUploadPartResponseHeaders
    expires_at: datetime.datetime
    part_size_bytes: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.presign_file_upload_part_response_headers import PresignFileUploadPartResponseHeaders
        transport = self.transport

        part_number = self.part_number

        url = self.url

        headers = self.headers.to_dict()

        expires_at = self.expires_at.isoformat()

        part_size_bytes = self.part_size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "partNumber": part_number,
            "url": url,
            "headers": headers,
            "expiresAt": expires_at,
            "partSizeBytes": part_size_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.presign_file_upload_part_response_headers import PresignFileUploadPartResponseHeaders
        d = dict(src_dict)
        transport = cast(Literal['presigned-multipart'] , d.pop("transport"))
        if transport != 'presigned-multipart':
            raise ValueError(f"transport must match const 'presigned-multipart', got '{transport}'")

        part_number = d.pop("partNumber")

        url = d.pop("url")

        headers = PresignFileUploadPartResponseHeaders.from_dict(d.pop("headers"))




        expires_at = isoparse(d.pop("expiresAt"))




        part_size_bytes = d.pop("partSizeBytes")

        presign_file_upload_part_response = cls(
            transport=transport,
            part_number=part_number,
            url=url,
            headers=headers,
            expires_at=expires_at,
            part_size_bytes=part_size_bytes,
        )

        return presign_file_upload_part_response
