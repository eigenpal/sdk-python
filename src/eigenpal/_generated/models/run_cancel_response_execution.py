from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus






T = TypeVar("T", bound="RunCancelResponseExecution")



@_attrs_define
class RunCancelResponseExecution:
    """
        Attributes:
            status (ExecutionStatus):
     """

    status: ExecutionStatus





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ExecutionStatus(d.pop("status"))




        run_cancel_response_execution = cls(
            status=status,
        )

        return run_cancel_response_execution
