from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus






T = TypeVar("T", bound="RerunAgentExecutionResponse")



@_attrs_define
class RerunAgentExecutionResponse:
    """ 
        Attributes:
            execution_id (str):
            source_execution_id (str):
            status (ExecutionStatus):
     """

    execution_id: str
    source_execution_id: str
    status: ExecutionStatus





    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        source_execution_id = self.source_execution_id

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "executionId": execution_id,
            "sourceExecutionId": source_execution_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        source_execution_id = d.pop("sourceExecutionId")

        status = ExecutionStatus(d.pop("status"))




        rerun_agent_execution_response = cls(
            execution_id=execution_id,
            source_execution_id=source_execution_id,
            status=status,
        )

        return rerun_agent_execution_response

