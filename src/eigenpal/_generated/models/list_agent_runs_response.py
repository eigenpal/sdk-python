from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_summary import AgentExecutionSummary





T = TypeVar("T", bound="ListAgentRunsResponse")



@_attrs_define
class ListAgentRunsResponse:
    """ 
        Attributes:
            runs (list[AgentExecutionSummary]):
            total (int):
            limit (int):
            offset (int):
            scan_limited (bool | Unset):
            no_resolved_anchor (bool | Unset):
     """

    runs: list[AgentExecutionSummary]
    total: int
    limit: int
    offset: int
    scan_limited: bool | Unset = UNSET
    no_resolved_anchor: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_summary import AgentExecutionSummary
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)



        total = self.total

        limit = self.limit

        offset = self.offset

        scan_limited = self.scan_limited

        no_resolved_anchor = self.no_resolved_anchor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runs": runs,
            "total": total,
            "limit": limit,
            "offset": offset,
        })
        if scan_limited is not UNSET:
            field_dict["scanLimited"] = scan_limited
        if no_resolved_anchor is not UNSET:
            field_dict["noResolvedAnchor"] = no_resolved_anchor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_summary import AgentExecutionSummary
        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in (_runs):
            runs_item = AgentExecutionSummary.from_dict(runs_item_data)



            runs.append(runs_item)


        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        scan_limited = d.pop("scanLimited", UNSET)

        no_resolved_anchor = d.pop("noResolvedAnchor", UNSET)

        list_agent_runs_response = cls(
            runs=runs,
            total=total,
            limit=limit,
            offset=offset,
            scan_limited=scan_limited,
            no_resolved_anchor=no_resolved_anchor,
        )

        return list_agent_runs_response

