from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="RunWorkflowResponse")



@_attrs_define
class RunWorkflowResponse:
    """ 
        Attributes:
            execution_id (str): Newly created execution id (e.g. exec_xyz)
            status (ExecutionStatus | Unset):
            result (Any | Unset): Workflow output (status=completed)
            error (str | Unset): Error message (status=failed)
     """

    execution_id: str
    status: ExecutionStatus | Unset = UNSET
    result: Any | Unset = UNSET
    error: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        result = self.result

        error = self.error


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executionId": execution_id,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        _status = d.pop("status", UNSET)
        status: ExecutionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ExecutionStatus(_status)




        result = d.pop("result", UNSET)

        error = d.pop("error", UNSET)

        run_workflow_response = cls(
            execution_id=execution_id,
            status=status,
            result=result,
            error=error,
        )

        return run_workflow_response

