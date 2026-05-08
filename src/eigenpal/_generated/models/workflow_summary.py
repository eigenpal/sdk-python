from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_summary_current_version_type_0 import WorkflowSummaryCurrentVersionType0





T = TypeVar("T", bound="WorkflowSummary")



@_attrs_define
class WorkflowSummary:
    """ 
        Attributes:
            id (str):
            tenant_id (str):
            created_at (str):
            is_block (bool | Unset):
            updated_at (str | Unset):
            current_version (None | Unset | WorkflowSummaryCurrentVersionType0):
     """

    id: str
    tenant_id: str
    created_at: str
    is_block: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    current_version: None | Unset | WorkflowSummaryCurrentVersionType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_summary_current_version_type_0 import WorkflowSummaryCurrentVersionType0
        id = self.id

        tenant_id = self.tenant_id

        created_at: str
        created_at = self.created_at

        is_block = self.is_block

        updated_at: str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        current_version: dict[str, Any] | None | Unset
        if isinstance(self.current_version, Unset):
            current_version = UNSET
        elif isinstance(self.current_version, WorkflowSummaryCurrentVersionType0):
            current_version = self.current_version.to_dict()
        else:
            current_version = self.current_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "tenantId": tenant_id,
            "createdAt": created_at,
        })
        if is_block is not UNSET:
            field_dict["isBlock"] = is_block
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_summary_current_version_type_0 import WorkflowSummaryCurrentVersionType0
        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenantId")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        is_block = d.pop("isBlock", UNSET)

        def _parse_updated_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_current_version(data: object) -> None | Unset | WorkflowSummaryCurrentVersionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_version_type_0 = WorkflowSummaryCurrentVersionType0.from_dict(data)



                return current_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowSummaryCurrentVersionType0, data)

        current_version = _parse_current_version(d.pop("currentVersion", UNSET))


        workflow_summary = cls(
            id=id,
            tenant_id=tenant_id,
            created_at=created_at,
            is_block=is_block,
            updated_at=updated_at,
            current_version=current_version,
        )


        workflow_summary.additional_properties = d
        return workflow_summary

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
