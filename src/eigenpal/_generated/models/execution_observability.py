from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_observability_current_phase import ExecutionObservabilityCurrentPhase
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.execution_observability_failure import ExecutionObservabilityFailure
  from ..models.execution_observability_phases_item import ExecutionObservabilityPhasesItem





T = TypeVar("T", bound="ExecutionObservability")



@_attrs_define
class ExecutionObservability:
    """ 
        Attributes:
            phases (list[ExecutionObservabilityPhasesItem]):
            derived (bool):
            current_phase (ExecutionObservabilityCurrentPhase | Unset):
            failure (ExecutionObservabilityFailure | Unset):
     """

    phases: list[ExecutionObservabilityPhasesItem]
    derived: bool
    current_phase: ExecutionObservabilityCurrentPhase | Unset = UNSET
    failure: ExecutionObservabilityFailure | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_observability_failure import ExecutionObservabilityFailure
        from ..models.execution_observability_phases_item import ExecutionObservabilityPhasesItem
        phases = []
        for phases_item_data in self.phases:
            phases_item = phases_item_data.to_dict()
            phases.append(phases_item)



        derived = self.derived

        current_phase: str | Unset = UNSET
        if not isinstance(self.current_phase, Unset):
            current_phase = self.current_phase.value


        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "phases": phases,
            "derived": derived,
        })
        if current_phase is not UNSET:
            field_dict["currentPhase"] = current_phase
        if failure is not UNSET:
            field_dict["failure"] = failure

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_observability_failure import ExecutionObservabilityFailure
        from ..models.execution_observability_phases_item import ExecutionObservabilityPhasesItem
        d = dict(src_dict)
        phases = []
        _phases = d.pop("phases")
        for phases_item_data in (_phases):
            phases_item = ExecutionObservabilityPhasesItem.from_dict(phases_item_data)



            phases.append(phases_item)


        derived = d.pop("derived")

        _current_phase = d.pop("currentPhase", UNSET)
        current_phase: ExecutionObservabilityCurrentPhase | Unset
        if isinstance(_current_phase,  Unset):
            current_phase = UNSET
        else:
            current_phase = ExecutionObservabilityCurrentPhase(_current_phase)




        _failure = d.pop("failure", UNSET)
        failure: ExecutionObservabilityFailure | Unset
        if isinstance(_failure,  Unset):
            failure = UNSET
        else:
            failure = ExecutionObservabilityFailure.from_dict(_failure)




        execution_observability = cls(
            phases=phases,
            derived=derived,
            current_phase=current_phase,
            failure=failure,
        )

        return execution_observability

