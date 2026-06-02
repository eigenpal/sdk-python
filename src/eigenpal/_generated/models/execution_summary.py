from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.execution_summary_workflow_type_0 import ExecutionSummaryWorkflowType0





T = TypeVar("T", bound="ExecutionSummary")



@_attrs_define
class ExecutionSummary:
    """ 
        Attributes:
            id (str):
            workflow_id (str):
            status (ExecutionStatus):
            created_at (str):
            trigger_type (None | str | Unset): "api" | "scheduled" | "manual" | …
            trigger_input (Any | None | Unset): Original input map. Useful for replay.
            result (Any | None | Unset): Workflow output (status=completed).
            error (None | str | Unset): Error message (status=failed).
            started_at (None | str | Unset):
            completed_at (None | str | Unset):
            duration_ms (int | None | Unset): Total wall-clock duration in milliseconds. Only set after the execution
                reaches a terminal status.
            workflow (ExecutionSummaryWorkflowType0 | None | Unset): Owning workflow (null when the workflow has been
                deleted)
     """

    id: str
    workflow_id: str
    status: ExecutionStatus
    created_at: str
    trigger_type: None | str | Unset = UNSET
    trigger_input: Any | None | Unset = UNSET
    result: Any | None | Unset = UNSET
    error: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    workflow: ExecutionSummaryWorkflowType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_summary_workflow_type_0 import ExecutionSummaryWorkflowType0
        id = self.id

        workflow_id = self.workflow_id

        status = self.status.value

        created_at: str
        created_at = self.created_at

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        trigger_input: Any | None | Unset
        if isinstance(self.trigger_input, Unset):
            trigger_input = UNSET
        else:
            trigger_input = self.trigger_input

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

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        workflow: dict[str, Any] | None | Unset
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        elif isinstance(self.workflow, ExecutionSummaryWorkflowType0):
            workflow = self.workflow.to_dict()
        else:
            workflow = self.workflow


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "workflowId": workflow_id,
            "status": status,
            "createdAt": created_at,
        })
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type
        if trigger_input is not UNSET:
            field_dict["triggerInput"] = trigger_input
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_summary_workflow_type_0 import ExecutionSummaryWorkflowType0
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        status = ExecutionStatus(d.pop("status"))




        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_trigger_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("triggerType", UNSET))


        def _parse_trigger_input(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        trigger_input = _parse_trigger_input(d.pop("triggerInput", UNSET))


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


        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))


        def _parse_workflow(data: object) -> ExecutionSummaryWorkflowType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workflow_type_0 = ExecutionSummaryWorkflowType0.from_dict(data)



                return workflow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionSummaryWorkflowType0 | None | Unset, data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))


        execution_summary = cls(
            id=id,
            workflow_id=workflow_id,
            status=status,
            created_at=created_at,
            trigger_type=trigger_type,
            trigger_input=trigger_input,
            result=result,
            error=error,
            started_at=started_at,
            completed_at=completed_at,
            duration_ms=duration_ms,
            workflow=workflow,
        )

        return execution_summary

