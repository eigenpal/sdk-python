from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.human_review_list_response_tasks_item import HumanReviewListResponseTasksItem





T = TypeVar("T", bound="HumanReviewListResponse")



@_attrs_define
class HumanReviewListResponse:
    """
        Attributes:
            tasks (list[HumanReviewListResponseTasksItem]):
            next_cursor (None | str):
     """

    tasks: list[HumanReviewListResponseTasksItem]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.human_review_list_response_tasks_item import HumanReviewListResponseTasksItem
        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tasks": tasks,
            "nextCursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_review_list_response_tasks_item import HumanReviewListResponseTasksItem
        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in (_tasks):
            tasks_item = HumanReviewListResponseTasksItem.from_dict(tasks_item_data)



            tasks.append(tasks_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))


        human_review_list_response = cls(
            tasks=tasks,
            next_cursor=next_cursor,
        )

        return human_review_list_response
