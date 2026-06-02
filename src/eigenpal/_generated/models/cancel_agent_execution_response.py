from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_summary import AgentExecutionSummary





T = TypeVar("T", bound="CancelAgentExecutionResponse")



@_attrs_define
class CancelAgentExecutionResponse:
    """ 
        Attributes:
            run (AgentExecutionSummary):
     """

    run: AgentExecutionSummary





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_summary import AgentExecutionSummary
        run = self.run.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "run": run,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_summary import AgentExecutionSummary
        d = dict(src_dict)
        run = AgentExecutionSummary.from_dict(d.pop("run"))




        cancel_agent_execution_response = cls(
            run=run,
        )

        return cancel_agent_execution_response

