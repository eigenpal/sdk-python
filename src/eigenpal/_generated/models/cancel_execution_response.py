from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_execution_response_status import CancelExecutionResponseStatus
from ..models.execution_status import ExecutionStatus






T = TypeVar("T", bound="CancelExecutionResponse")



@_attrs_define
class CancelExecutionResponse:
    """ 
        Attributes:
            execution_id (str):
            status (CancelExecutionResponseStatus): Outcome. `cancelled` (transitioned), `cancellation-requested` (worker
                will observe), or `already-terminal` (no-op).
            was_status (ExecutionStatus):
     """

    execution_id: str
    status: CancelExecutionResponseStatus
    was_status: ExecutionStatus





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        status = self.status.value

        was_status = self.was_status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executionId": execution_id,
            "status": status,
            "wasStatus": was_status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        status = CancelExecutionResponseStatus(d.pop("status"))




        was_status = ExecutionStatus(d.pop("wasStatus"))




        cancel_execution_response = cls(
            execution_id=execution_id,
            status=status,
            was_status=was_status,
        )

        return cancel_execution_response

