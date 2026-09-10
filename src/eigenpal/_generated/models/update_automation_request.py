from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAutomationRequest")



@_attrs_define
class UpdateAutomationRequest:
    """
        Attributes:
            folder_id (None | str | Unset): Move a YAML workflow into this workflow folder. `null` files it at the tenant
                root. Ignored for the folder lookup when `folderPath` is also sent, but a string value is still validated before
                the path is applied.
            folder_path (str | Unset): Slash-separated workflow folder path. Missing folders are created. Empty or `/` means
                root. When both fields are sent, `folderPath` wins after `folderId` validation.
     """

    folder_id: None | str | Unset = UNSET
    folder_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        folder_id: None | str | Unset
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        folder_path = self.folder_path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if folder_path is not UNSET:
            field_dict["folderPath"] = folder_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_folder_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_id = _parse_folder_id(d.pop("folderId", UNSET))


        folder_path = d.pop("folderPath", UNSET)

        update_automation_request = cls(
            folder_id=folder_id,
            folder_path=folder_path,
        )


        update_automation_request.additional_properties = d
        return update_automation_request

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
