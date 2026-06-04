from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_observability_phases_item_phase import ExecutionObservabilityPhasesItemPhase
from ..models.execution_observability_phases_item_status import ExecutionObservabilityPhasesItemStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExecutionObservabilityPhasesItem")



@_attrs_define
class ExecutionObservabilityPhasesItem:
    """ 
        Attributes:
            execution_id (str):
            phase (ExecutionObservabilityPhasesItemPhase):
            phase_order (int):
            status (ExecutionObservabilityPhasesItemStatus):
            started_at (None | str | Unset):
            completed_at (None | str | Unset):
            message (None | str | Unset):
            failure_code (None | str | Unset):
            duration_ms (int | None | Unset):
     """

    execution_id: str
    phase: ExecutionObservabilityPhasesItemPhase
    phase_order: int
    status: ExecutionObservabilityPhasesItemStatus
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    failure_code: None | str | Unset = UNSET
    duration_ms: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        phase = self.phase.value

        phase_order = self.phase_order

        status = self.status.value

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        failure_code: None | str | Unset
        if isinstance(self.failure_code, Unset):
            failure_code = UNSET
        else:
            failure_code = self.failure_code

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executionId": execution_id,
            "phase": phase,
            "phaseOrder": phase_order,
            "status": status,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if message is not UNSET:
            field_dict["message"] = message
        if failure_code is not UNSET:
            field_dict["failureCode"] = failure_code
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        phase = ExecutionObservabilityPhasesItemPhase(d.pop("phase"))




        phase_order = d.pop("phaseOrder")

        status = ExecutionObservabilityPhasesItemStatus(d.pop("status"))




        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        def _parse_failure_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_code = _parse_failure_code(d.pop("failureCode", UNSET))


        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))


        execution_observability_phases_item = cls(
            execution_id=execution_id,
            phase=phase,
            phase_order=phase_order,
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            message=message,
            failure_code=failure_code,
            duration_ms=duration_ms,
        )

        return execution_observability_phases_item

