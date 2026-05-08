from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WorkflowSummaryCurrentVersionType0")



@_attrs_define
class WorkflowSummaryCurrentVersionType0:
    """ 
        Attributes:
            id (str | Unset):
            version (None | str | Unset):
            yaml_content (str | Unset):
            definition (Any | Unset):
            message (None | str | Unset):
            created_at (str | Unset):
     """

    id: str | Unset = UNSET
    version: None | str | Unset = UNSET
    yaml_content: str | Unset = UNSET
    definition: Any | Unset = UNSET
    message: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        yaml_content = self.yaml_content

        definition = self.definition

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        created_at: str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if yaml_content is not UNSET:
            field_dict["yamlContent"] = yaml_content
        if definition is not UNSET:
            field_dict["definition"] = definition
        if message is not UNSET:
            field_dict["message"] = message
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        yaml_content = d.pop("yamlContent", UNSET)

        definition = d.pop("definition", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        def _parse_created_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        workflow_summary_current_version_type_0 = cls(
            id=id,
            version=version,
            yaml_content=yaml_content,
            definition=definition,
            message=message,
            created_at=created_at,
        )


        workflow_summary_current_version_type_0.additional_properties = d
        return workflow_summary_current_version_type_0

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
