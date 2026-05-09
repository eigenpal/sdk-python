from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_summary import AgentSummary





T = TypeVar("T", bound="GetAgentResponse")



@_attrs_define
class GetAgentResponse:
    """ 
        Attributes:
            agent (AgentSummary):
     """

    agent: AgentSummary





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_summary import AgentSummary
        agent = self.agent.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_summary import AgentSummary
        d = dict(src_dict)
        agent = AgentSummary.from_dict(d.pop("agent"))




        get_agent_response = cls(
            agent=agent,
        )

        return get_agent_response

