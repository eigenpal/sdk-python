from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..models.run_cancel_response_cancellation_state import RunCancelResponseCancellationState






T = TypeVar("T", bound="RunCancelResponseCancellation")



@_attrs_define
class RunCancelResponseCancellation:
    """
        Attributes:
            state (RunCancelResponseCancellationState): `cancelled` — the run was terminated immediately (it had not
                started). `requested` — the run is in-flight; cancellation was requested and the status will become `cancelled`
                shortly. `already_terminal` — the run had already finished; nothing changed.
            was_status (ExecutionStatus):
     """

    state: RunCancelResponseCancellationState
    was_status: ExecutionStatus





    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        was_status = self.was_status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "state": state,
            "wasStatus": was_status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = RunCancelResponseCancellationState(d.pop("state"))




        was_status = ExecutionStatus(d.pop("wasStatus"))




        run_cancel_response_cancellation = cls(
            state=state,
            was_status=was_status,
        )

        return run_cancel_response_cancellation
