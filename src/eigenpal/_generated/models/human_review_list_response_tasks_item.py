from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_list_response_tasks_item_source_kind import HumanReviewListResponseTasksItemSourceKind
from ..models.human_review_list_response_tasks_item_status import HumanReviewListResponseTasksItemStatus






T = TypeVar("T", bound="HumanReviewListResponseTasksItem")



@_attrs_define
class HumanReviewListResponseTasksItem:
    """
        Attributes:
            id (str):
            execution_id (str):
            automation_id (str):
            automation_name (str):
            source_kind (HumanReviewListResponseTasksItemSourceKind):
            source_label (str):
            status (HumanReviewListResponseTasksItemStatus):
            required_count (int):
            confirmed_count (int):
            version (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    execution_id: str
    automation_id: str
    automation_name: str
    source_kind: HumanReviewListResponseTasksItemSourceKind
    source_label: str
    status: HumanReviewListResponseTasksItemStatus
    required_count: int
    confirmed_count: int
    version: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        execution_id = self.execution_id

        automation_id = self.automation_id

        automation_name = self.automation_name

        source_kind = self.source_kind.value

        source_label = self.source_label

        status = self.status.value

        required_count = self.required_count

        confirmed_count = self.confirmed_count

        version = self.version

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "executionId": execution_id,
            "automationId": automation_id,
            "automationName": automation_name,
            "sourceKind": source_kind,
            "sourceLabel": source_label,
            "status": status,
            "requiredCount": required_count,
            "confirmedCount": confirmed_count,
            "version": version,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        execution_id = d.pop("executionId")

        automation_id = d.pop("automationId")

        automation_name = d.pop("automationName")

        source_kind = HumanReviewListResponseTasksItemSourceKind(d.pop("sourceKind"))




        source_label = d.pop("sourceLabel")

        status = HumanReviewListResponseTasksItemStatus(d.pop("status"))




        required_count = d.pop("requiredCount")

        confirmed_count = d.pop("confirmedCount")

        version = d.pop("version")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        human_review_list_response_tasks_item = cls(
            id=id,
            execution_id=execution_id,
            automation_id=automation_id,
            automation_name=automation_name,
            source_kind=source_kind,
            source_label=source_label,
            status=status,
            required_count=required_count,
            confirmed_count=confirmed_count,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
        )

        return human_review_list_response_tasks_item
