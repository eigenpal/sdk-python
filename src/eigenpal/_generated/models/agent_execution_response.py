from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_summary import AgentExecutionSummary





T = TypeVar("T", bound="AgentExecutionResponse")



@_attrs_define
class AgentExecutionResponse:
    """ 
        Attributes:
            execution (AgentExecutionSummary):
     """

    execution: AgentExecutionSummary





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_summary import AgentExecutionSummary
        execution = self.execution.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "execution": execution,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_summary import AgentExecutionSummary
        d = dict(src_dict)
        execution = AgentExecutionSummary.from_dict(d.pop("execution"))




        agent_execution_response = cls(
            execution=execution,
        )

        return agent_execution_response

