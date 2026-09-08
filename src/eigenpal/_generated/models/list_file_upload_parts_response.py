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
  from ..models.list_file_upload_parts_response_parts_item import ListFileUploadPartsResponsePartsItem





T = TypeVar("T", bound="ListFileUploadPartsResponse")



@_attrs_define
class ListFileUploadPartsResponse:
    """
        Attributes:
            transport (Literal['presigned-multipart']):
            upload_id (str):
            file_id (str):
            part_size_bytes (int):
            part_count (int):
            expires_at (datetime.datetime):
            parts (list[ListFileUploadPartsResponsePartsItem]):
     """

    transport: Literal['presigned-multipart']
    upload_id: str
    file_id: str
    part_size_bytes: int
    part_count: int
    expires_at: datetime.datetime
    parts: list[ListFileUploadPartsResponsePartsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_file_upload_parts_response_parts_item import ListFileUploadPartsResponsePartsItem
        transport = self.transport

        upload_id = self.upload_id

        file_id = self.file_id

        part_size_bytes = self.part_size_bytes

        part_count = self.part_count

        expires_at = self.expires_at.isoformat()

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "uploadId": upload_id,
            "fileId": file_id,
            "partSizeBytes": part_size_bytes,
            "partCount": part_count,
            "expiresAt": expires_at,
            "parts": parts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_file_upload_parts_response_parts_item import ListFileUploadPartsResponsePartsItem
        d = dict(src_dict)
        transport = cast(Literal['presigned-multipart'] , d.pop("transport"))
        if transport != 'presigned-multipart':
            raise ValueError(f"transport must match const 'presigned-multipart', got '{transport}'")

        upload_id = d.pop("uploadId")

        file_id = d.pop("fileId")

        part_size_bytes = d.pop("partSizeBytes")

        part_count = d.pop("partCount")

        expires_at = isoparse(d.pop("expiresAt"))




        parts = []
        _parts = d.pop("parts")
        for parts_item_data in (_parts):
            parts_item = ListFileUploadPartsResponsePartsItem.from_dict(parts_item_data)



            parts.append(parts_item)


        list_file_upload_parts_response = cls(
            transport=transport,
            upload_id=upload_id,
            file_id=file_id,
            part_size_bytes=part_size_bytes,
            part_count=part_count,
            expires_at=expires_at,
            parts=parts,
        )

        return list_file_upload_parts_response
