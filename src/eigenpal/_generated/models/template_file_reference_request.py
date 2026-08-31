from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TemplateFileReferenceRequest")



@_attrs_define
class TemplateFileReferenceRequest:
    """
        Attributes:
            file_id (str): Reusable file id produced by the direct file upload flow. It is consumed as upload transport, not
                exposed as template identity.
            name (str | Unset):
            description (str | Unset):
            staged (bool | Unset): When true, the create response includes a one-time cleanupProof for unpublished CLI
                staging. Normal uploads omit this.
     """

    file_id: str
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    staged: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        name = self.name

        description = self.description

        staged = self.staged


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fileId": file_id,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if staged is not UNSET:
            field_dict["staged"] = staged

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        staged = d.pop("staged", UNSET)

        template_file_reference_request = cls(
            file_id=file_id,
            name=name,
            description=description,
            staged=staged,
        )


        template_file_reference_request.additional_properties = d
        return template_file_reference_request

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
