from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus






T = TypeVar("T", bound="RerunAgentRunResponse")



@_attrs_define
class RerunAgentRunResponse:
    """ 
        Attributes:
            run_id (str):
            source_run_id (str):
            status (ExecutionStatus):
     """

    run_id: str
    source_run_id: str
    status: ExecutionStatus





    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        source_run_id = self.source_run_id

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runId": run_id,
            "sourceRunId": source_run_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        source_run_id = d.pop("sourceRunId")

        status = ExecutionStatus(d.pop("status"))




        rerun_agent_run_response = cls(
            run_id=run_id,
            source_run_id=source_run_id,
            status=status,
        )

        return rerun_agent_run_response

