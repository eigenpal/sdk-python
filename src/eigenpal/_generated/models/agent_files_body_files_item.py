from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentFilesBodyFilesItem")



@_attrs_define
class AgentFilesBodyFilesItem:
    """ 
        Attributes:
            path (str):
            content (str | Unset):
            content_base_64 (str | Unset):
            content_type (str | Unset):
     """

    path: str
    content: str | Unset = UNSET
    content_base_64: str | Unset = UNSET
    content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        content_base_64 = self.content_base_64

        content_type = self.content_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
        })
        if content is not UNSET:
            field_dict["content"] = content
        if content_base_64 is not UNSET:
            field_dict["contentBase64"] = content_base_64
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        content = d.pop("content", UNSET)

        content_base_64 = d.pop("contentBase64", UNSET)

        content_type = d.pop("contentType", UNSET)

        agent_files_body_files_item = cls(
            path=path,
            content=content,
            content_base_64=content_base_64,
            content_type=content_type,
        )


        agent_files_body_files_item.additional_properties = d
        return agent_files_body_files_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
