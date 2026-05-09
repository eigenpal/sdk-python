from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WorkflowVersion")



@_attrs_define
class WorkflowVersion:
    """ 
        Attributes:
            id (str): Version id (e.g. wfh_xyz). Stable for SDK pinning.
            workflow_id (str):
            version (None | str | Unset): Release tag for this version.
            yaml_content (str | Unset): Workflow YAML at this version.
            is_current (bool | Unset): True when this is the workflow’s currently published version.
            created_at (str | Unset):
     """

    id: str
    workflow_id: str
    version: None | str | Unset = UNSET
    yaml_content: str | Unset = UNSET
    is_current: bool | Unset = UNSET
    created_at: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        yaml_content = self.yaml_content

        is_current = self.is_current

        created_at: str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "workflowId": workflow_id,
        })
        if version is not UNSET:
            field_dict["version"] = version
        if yaml_content is not UNSET:
            field_dict["yamlContent"] = yaml_content
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        yaml_content = d.pop("yamlContent", UNSET)

        is_current = d.pop("isCurrent", UNSET)

        def _parse_created_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        workflow_version = cls(
            id=id,
            workflow_id=workflow_id,
            version=version,
            yaml_content=yaml_content,
            is_current=is_current,
            created_at=created_at,
        )

        return workflow_version

