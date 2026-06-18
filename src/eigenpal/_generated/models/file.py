from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="File")



@_attrs_define
class File:
    """
        Attributes:
            id (str):
            filename (str):
            content_type (None | str):
            size (int | None):
            created_at (str):
            purpose (None | str | Unset):
     """

    id: str
    filename: str
    content_type: None | str
    size: int | None
    created_at: str
    purpose: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        content_type: None | str
        content_type = self.content_type

        size: int | None
        size = self.size

        created_at: str
        created_at = self.created_at

        purpose: None | str | Unset
        if isinstance(self.purpose, Unset):
            purpose = UNSET
        else:
            purpose = self.purpose


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "filename": filename,
            "contentType": content_type,
            "size": size,
            "createdAt": created_at,
        })
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        def _parse_content_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_type = _parse_content_type(d.pop("contentType"))


        def _parse_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size = _parse_size(d.pop("size"))


        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_purpose(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purpose = _parse_purpose(d.pop("purpose", UNSET))


        file = cls(
            id=id,
            filename=filename,
            content_type=content_type,
            size=size,
            created_at=created_at,
            purpose=purpose,
        )

        return file
