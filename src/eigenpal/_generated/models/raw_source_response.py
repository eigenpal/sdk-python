from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RawSourceResponse")



@_attrs_define
class RawSourceResponse:
    """ 
        Attributes:
            ref (str):
            path (str):
            content_type (str):
            content (str):
     """

    ref: str
    path: str
    content_type: str
    content: str





    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        path = self.path

        content_type = self.content_type

        content = self.content


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ref": ref,
            "path": path,
            "contentType": content_type,
            "content": content,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref = d.pop("ref")

        path = d.pop("path")

        content_type = d.pop("contentType")

        content = d.pop("content")

        raw_source_response = cls(
            ref=ref,
            path=path,
            content_type=content_type,
            content=content,
        )

        return raw_source_response

