from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListFileUploadPartsResponsePartsItem")



@_attrs_define
class ListFileUploadPartsResponsePartsItem:
    """
        Attributes:
            part_number (int):
            etag (str):
            size (int | Unset):
     """

    part_number: int
    etag: str
    size: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        etag = self.etag

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "partNumber": part_number,
            "etag": etag,
        })
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        part_number = d.pop("partNumber")

        etag = d.pop("etag")

        size = d.pop("size", UNSET)

        list_file_upload_parts_response_parts_item = cls(
            part_number=part_number,
            etag=etag,
            size=size,
        )

        return list_file_upload_parts_response_parts_item
