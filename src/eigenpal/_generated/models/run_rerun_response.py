from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunRerunResponse")



@_attrs_define
class RunRerunResponse:
    """ 
        Attributes:
            execution_id (str | Unset):
            run_id (str | Unset):
            status (str | Unset):
     """

    execution_id: str | Unset = UNSET
    run_id: str | Unset = UNSET
    status: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        run_id = self.run_id

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId", UNSET)

        run_id = d.pop("runId", UNSET)

        status = d.pop("status", UNSET)

        run_rerun_response = cls(
            execution_id=execution_id,
            run_id=run_id,
            status=status,
        )

        return run_rerun_response

