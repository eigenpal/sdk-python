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






T = TypeVar("T", bound="PresignedMultipartFileUploadSession")



@_attrs_define
class PresignedMultipartFileUploadSession:
    """
        Attributes:
            transport (Literal['presigned-multipart']):
            upload_id (str):
            file_id (str):
            part_size_bytes (int):
            part_count (int):
            parts_url (str):
            complete_url (str):
            expires_at (datetime.datetime):
            max_file_size_bytes (int):
     """

    transport: Literal['presigned-multipart']
    upload_id: str
    file_id: str
    part_size_bytes: int
    part_count: int
    parts_url: str
    complete_url: str
    expires_at: datetime.datetime
    max_file_size_bytes: int





    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        upload_id = self.upload_id

        file_id = self.file_id

        part_size_bytes = self.part_size_bytes

        part_count = self.part_count

        parts_url = self.parts_url

        complete_url = self.complete_url

        expires_at = self.expires_at.isoformat()

        max_file_size_bytes = self.max_file_size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "uploadId": upload_id,
            "fileId": file_id,
            "partSizeBytes": part_size_bytes,
            "partCount": part_count,
            "partsUrl": parts_url,
            "completeUrl": complete_url,
            "expiresAt": expires_at,
            "maxFileSizeBytes": max_file_size_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transport = cast(Literal['presigned-multipart'] , d.pop("transport"))
        if transport != 'presigned-multipart':
            raise ValueError(f"transport must match const 'presigned-multipart', got '{transport}'")

        upload_id = d.pop("uploadId")

        file_id = d.pop("fileId")

        part_size_bytes = d.pop("partSizeBytes")

        part_count = d.pop("partCount")

        parts_url = d.pop("partsUrl")

        complete_url = d.pop("completeUrl")

        expires_at = isoparse(d.pop("expiresAt"))




        max_file_size_bytes = d.pop("maxFileSizeBytes")

        presigned_multipart_file_upload_session = cls(
            transport=transport,
            upload_id=upload_id,
            file_id=file_id,
            part_size_bytes=part_size_bytes,
            part_count=part_count,
            parts_url=parts_url,
            complete_url=complete_url,
            expires_at=expires_at,
            max_file_size_bytes=max_file_size_bytes,
        )

        return presigned_multipart_file_upload_session
