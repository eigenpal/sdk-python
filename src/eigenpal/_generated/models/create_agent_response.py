from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_agent_response_recovery_kind import CreateAgentResponseRecoveryKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_summary import AgentSummary





T = TypeVar("T", bound="CreateAgentResponse")



@_attrs_define
class CreateAgentResponse:
    """ 
        Attributes:
            agent (AgentSummary):
            source_recovered (bool | Unset):
            recovery_kind (CreateAgentResponseRecoveryKind | Unset):
     """

    agent: AgentSummary
    source_recovered: bool | Unset = UNSET
    recovery_kind: CreateAgentResponseRecoveryKind | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_summary import AgentSummary
        agent = self.agent.to_dict()

        source_recovered = self.source_recovered

        recovery_kind: str | Unset = UNSET
        if not isinstance(self.recovery_kind, Unset):
            recovery_kind = self.recovery_kind.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
        })
        if source_recovered is not UNSET:
            field_dict["sourceRecovered"] = source_recovered
        if recovery_kind is not UNSET:
            field_dict["recoveryKind"] = recovery_kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_summary import AgentSummary
        d = dict(src_dict)
        agent = AgentSummary.from_dict(d.pop("agent"))




        source_recovered = d.pop("sourceRecovered", UNSET)

        _recovery_kind = d.pop("recoveryKind", UNSET)
        recovery_kind: CreateAgentResponseRecoveryKind | Unset
        if isinstance(_recovery_kind,  Unset):
            recovery_kind = UNSET
        else:
            recovery_kind = CreateAgentResponseRecoveryKind(_recovery_kind)




        create_agent_response = cls(
            agent=agent,
            source_recovered=source_recovered,
            recovery_kind=recovery_kind,
        )

        return create_agent_response

