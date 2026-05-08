from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExecutionStatusResponse")



@_attrs_define
class ExecutionStatusResponse:
    """ 
        Attributes:
            execution_id (str):
            status (ExecutionStatus):
            created_at (str): ISO-8601 creation timestamp
            completed_at (None | str | Unset): ISO-8601 completion timestamp; only set in terminal states
            result (Any | None | Unset): Workflow output (status=completed)
            error (None | str | Unset): Error message (status=failed)
     """

    execution_id: str
    status: ExecutionStatus
    created_at: str
    completed_at: None | str | Unset = UNSET
    result: Any | None | Unset = UNSET
    error: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        status = self.status.value

        created_at = self.created_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        result: Any | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executionId": execution_id,
            "status": status,
            "createdAt": created_at,
        })
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        status = ExecutionStatus(d.pop("status"))




        created_at = d.pop("createdAt")

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_result(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        execution_status_response = cls(
            execution_id=execution_id,
            status=status,
            created_at=created_at,
            completed_at=completed_at,
            result=result,
            error=error,
        )

        return execution_status_response

