from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_upload_session_transport import FileUploadSessionTransport
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.file_upload_session_parts_item import FileUploadSessionPartsItem





T = TypeVar("T", bound="FileUploadSession")



@_attrs_define
class FileUploadSession:
    """
        Attributes:
            upload_id (str):
            file_id (str):
            transport (FileUploadSessionTransport):
            status (str):
            expires_at (datetime.datetime):
            part_size_bytes (int | None | Unset):
            part_count (int | None | Unset):
            parts (list[FileUploadSessionPartsItem] | Unset):
     """

    upload_id: str
    file_id: str
    transport: FileUploadSessionTransport
    status: str
    expires_at: datetime.datetime
    part_size_bytes: int | None | Unset = UNSET
    part_count: int | None | Unset = UNSET
    parts: list[FileUploadSessionPartsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_upload_session_parts_item import FileUploadSessionPartsItem
        upload_id = self.upload_id

        file_id = self.file_id

        transport = self.transport.value

        status = self.status

        expires_at = self.expires_at.isoformat()

        part_size_bytes: int | None | Unset
        if isinstance(self.part_size_bytes, Unset):
            part_size_bytes = UNSET
        else:
            part_size_bytes = self.part_size_bytes

        part_count: int | None | Unset
        if isinstance(self.part_count, Unset):
            part_count = UNSET
        else:
            part_count = self.part_count

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "uploadId": upload_id,
            "fileId": file_id,
            "transport": transport,
            "status": status,
            "expiresAt": expires_at,
        })
        if part_size_bytes is not UNSET:
            field_dict["partSizeBytes"] = part_size_bytes
        if part_count is not UNSET:
            field_dict["partCount"] = part_count
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_upload_session_parts_item import FileUploadSessionPartsItem
        d = dict(src_dict)
        upload_id = d.pop("uploadId")

        file_id = d.pop("fileId")

        transport = FileUploadSessionTransport(d.pop("transport"))




        status = d.pop("status")

        expires_at = isoparse(d.pop("expiresAt"))




        def _parse_part_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        part_size_bytes = _parse_part_size_bytes(d.pop("partSizeBytes", UNSET))


        def _parse_part_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        part_count = _parse_part_count(d.pop("partCount", UNSET))


        _parts = d.pop("parts", UNSET)
        parts: list[FileUploadSessionPartsItem] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = FileUploadSessionPartsItem.from_dict(parts_item_data)



                parts.append(parts_item)


        file_upload_session = cls(
            upload_id=upload_id,
            file_id=file_id,
            transport=transport,
            status=status,
            expires_at=expires_at,
            part_size_bytes=part_size_bytes,
            part_count=part_count,
            parts=parts,
        )

        return file_upload_session
