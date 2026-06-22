from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunTraceEvent")



@_attrs_define
class RunTraceEvent:
    """ Trace event emitted by a workflow or agent run. Extra fields depend on the run type and event source.

        Attributes:
            type_ (str | Unset): Event type when present. Agent traces mirror trace.jsonl events; workflow traces use
                execution phase or step records.
            phase (str | Unset): Workflow execution phase, when present.
            step_name (str | Unset): Workflow step name, when present.
            status (str | Unset): Event or execution status, when present.
            started_at (None | str | Unset): Event start timestamp.
            completed_at (None | str | Unset): Event completion timestamp.
            message (None | str | Unset): Human-readable event message.
     """

    type_: str | Unset = UNSET
    phase: str | Unset = UNSET
    step_name: str | Unset = UNSET
    status: str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        phase = self.phase

        step_name = self.step_name

        status = self.status

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if phase is not UNSET:
            field_dict["phase"] = phase
        if step_name is not UNSET:
            field_dict["stepName"] = step_name
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        phase = d.pop("phase", UNSET)

        step_name = d.pop("stepName", UNSET)

        status = d.pop("status", UNSET)

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


        run_trace_event = cls(
            type_=type_,
            phase=phase,
            step_name=step_name,
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            message=message,
        )


        run_trace_event.additional_properties = d
        return run_trace_event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
