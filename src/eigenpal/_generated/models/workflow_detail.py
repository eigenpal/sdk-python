from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WorkflowDetail")



@_attrs_define
class WorkflowDetail:
    """
        Attributes:
            id (str): Workflow id (e.g. wf_abc123).
            created_at (str):
            name (None | str | Unset): Human-readable workflow name from the YAML (e.g. "extract-invoice"). Null when no
                version is published yet.
            version (None | str | Unset): Current release tag (e.g. "1.2.4"). Null until a version is published.
            updated_at (str | Unset):
            yaml_content (None | str | Unset): YAML for the current version. Null until a version is published. Heavy; only
                returned on single-workflow GET, not on list.
     """

    id: str
    created_at: str
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    updated_at: str | Unset = UNSET
    yaml_content: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at: str
        created_at = self.created_at

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        updated_at: str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        yaml_content: None | str | Unset
        if isinstance(self.yaml_content, Unset):
            yaml_content = UNSET
        else:
            yaml_content = self.yaml_content


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "createdAt": created_at,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if yaml_content is not UNSET:
            field_dict["yamlContent"] = yaml_content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        def _parse_updated_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_yaml_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yaml_content = _parse_yaml_content(d.pop("yamlContent", UNSET))


        workflow_detail = cls(
            id=id,
            created_at=created_at,
            name=name,
            version=version,
            updated_at=updated_at,
            yaml_content=yaml_content,
        )

        return workflow_detail
