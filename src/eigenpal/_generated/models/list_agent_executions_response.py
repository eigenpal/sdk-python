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





T = TypeVar("T", bound="ListAgentExecutionsResponse")



@_attrs_define
class ListAgentExecutionsResponse:
    """ 
        Attributes:
            executions (list[AgentExecutionSummary]):
            total (int):
            limit (int):
            offset (int):
            scan_limited (bool | Unset):
            no_resolved_anchor (bool | Unset):
     """

    executions: list[AgentExecutionSummary]
    total: int
    limit: int
    offset: int
    scan_limited: bool | Unset = UNSET
    no_resolved_anchor: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_summary import AgentExecutionSummary
        executions = []
        for executions_item_data in self.executions:
            executions_item = executions_item_data.to_dict()
            executions.append(executions_item)



        total = self.total

        limit = self.limit

        offset = self.offset

        scan_limited = self.scan_limited

        no_resolved_anchor = self.no_resolved_anchor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executions": executions,
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
        executions = []
        _executions = d.pop("executions")
        for executions_item_data in (_executions):
            executions_item = AgentExecutionSummary.from_dict(executions_item_data)



            executions.append(executions_item)


        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        scan_limited = d.pop("scanLimited", UNSET)

        no_resolved_anchor = d.pop("noResolvedAnchor", UNSET)

        list_agent_executions_response = cls(
            executions=executions,
            total=total,
            limit=limit,
            offset=offset,
            scan_limited=scan_limited,
            no_resolved_anchor=no_resolved_anchor,
        )

        return list_agent_executions_response

