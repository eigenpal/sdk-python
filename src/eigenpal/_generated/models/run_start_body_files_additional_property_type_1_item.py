from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunStartBodyFilesAdditionalPropertyType1Item")



@_attrs_define
class RunStartBodyFilesAdditionalPropertyType1Item:
    """
        Attributes:
            file_id (str):
            filename (str | Unset):
            mime_type (str | Unset):
     """

    file_id: str
    filename: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        filename = self.filename

        mime_type = self.mime_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fileId": file_id,
        })
        if filename is not UNSET:
            field_dict["filename"] = filename
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId")

        filename = d.pop("filename", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        run_start_body_files_additional_property_type_1_item = cls(
            file_id=file_id,
            filename=filename,
            mime_type=mime_type,
        )


        run_start_body_files_additional_property_type_1_item.additional_properties = d
        return run_start_body_files_additional_property_type_1_item

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
