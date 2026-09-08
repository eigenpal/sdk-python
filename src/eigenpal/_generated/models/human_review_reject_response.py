from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.human_review_task_detail import HumanReviewTaskDetail





T = TypeVar("T", bound="HumanReviewRejectResponse")



@_attrs_define
class HumanReviewRejectResponse:
    """
        Attributes:
            task (HumanReviewTaskDetail):
     """

    task: HumanReviewTaskDetail





    def to_dict(self) -> dict[str, Any]:
        from ..models.human_review_task_detail import HumanReviewTaskDetail
        task = self.task.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "task": task,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_review_task_detail import HumanReviewTaskDetail
        d = dict(src_dict)
        task = HumanReviewTaskDetail.from_dict(d.pop("task"))




        human_review_reject_response = cls(
            task=task,
        )

        return human_review_reject_response
