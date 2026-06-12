from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_list_item import RunListItem





T = TypeVar("T", bound="RunsListResponse")



@_attrs_define
class RunsListResponse:
    """
        Attributes:
            runs (list[RunListItem]):
            next_cursor (None | str):
     """

    runs: list[RunListItem]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_list_item import RunListItem
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runs": runs,
            "nextCursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_list_item import RunListItem
        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in (_runs):
            runs_item = RunListItem.from_dict(runs_item_data)



            runs.append(runs_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))


        runs_list_response = cls(
            runs=runs,
            next_cursor=next_cursor,
        )

        return runs_list_response
