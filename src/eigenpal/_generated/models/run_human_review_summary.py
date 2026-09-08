from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_human_review_summary_source_kind import RunHumanReviewSummarySourceKind
from typing import Literal, cast






T = TypeVar("T", bound="RunHumanReviewSummary")



@_attrs_define
class RunHumanReviewSummary:
    """
        Attributes:
            task_id (str):
            source_kind (RunHumanReviewSummarySourceKind):
            source_label (str):
            status (Literal['pending']):
            required_count (int):
            confirmed_count (int):
            version (int):
     """

    task_id: str
    source_kind: RunHumanReviewSummarySourceKind
    source_label: str
    status: Literal['pending']
    required_count: int
    confirmed_count: int
    version: int





    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        source_kind = self.source_kind.value

        source_label = self.source_label

        status = self.status

        required_count = self.required_count

        confirmed_count = self.confirmed_count

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "taskId": task_id,
            "sourceKind": source_kind,
            "sourceLabel": source_label,
            "status": status,
            "requiredCount": required_count,
            "confirmedCount": confirmed_count,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId")

        source_kind = RunHumanReviewSummarySourceKind(d.pop("sourceKind"))




        source_label = d.pop("sourceLabel")

        status = cast(Literal['pending'] , d.pop("status"))
        if status != 'pending':
            raise ValueError(f"status must match const 'pending', got '{status}'")

        required_count = d.pop("requiredCount")

        confirmed_count = d.pop("confirmedCount")

        version = d.pop("version")

        run_human_review_summary = cls(
            task_id=task_id,
            source_kind=source_kind,
            source_label=source_label,
            status=status,
            required_count=required_count,
            confirmed_count=confirmed_count,
            version=version,
        )

        return run_human_review_summary
