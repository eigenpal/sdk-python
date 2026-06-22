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
  from ..models.run_execution_retry import RunExecutionRetry
  from ..models.run_feedback import RunFeedback
  from ..models.workflow_run_execution_expected import WorkflowRunExecutionExpected





T = TypeVar("T", bound="WorkflowRunExecution")



@_attrs_define
class WorkflowRunExecution:
    """
        Attributes:
            status (ExecutionStatus):
            schema_valid (bool | None): Whether the completed output matched the workflow or agent output schema.
            batch_id (None | str): Experiment batch id when the run is part of a batch.
            retry (RunExecutionRetry):
            steps (list[Any]): Per-step executions of the workflow run.
            definition_snapshot (Any | None | Unset): Workflow definition snapshot captured when the run was created.
            feedback (None | RunFeedback | Unset):
            expected (WorkflowRunExecutionExpected | Unset): Ground-truth expected output and files.
     """

    status: ExecutionStatus
    schema_valid: bool | None
    batch_id: None | str
    retry: RunExecutionRetry
    steps: list[Any]
    definition_snapshot: Any | None | Unset = UNSET
    feedback: None | RunFeedback | Unset = UNSET
    expected: WorkflowRunExecutionExpected | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_feedback import RunFeedback
        from ..models.workflow_run_execution_expected import WorkflowRunExecutionExpected
        status = self.status.value

        schema_valid: bool | None
        schema_valid = self.schema_valid

        batch_id: None | str
        batch_id = self.batch_id

        retry = self.retry.to_dict()

        steps = self.steps



        definition_snapshot: Any | None | Unset
        if isinstance(self.definition_snapshot, Unset):
            definition_snapshot = UNSET
        else:
            definition_snapshot = self.definition_snapshot

        feedback: dict[str, Any] | None | Unset
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        elif isinstance(self.feedback, RunFeedback):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        expected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected, Unset):
            expected = self.expected.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "schemaValid": schema_valid,
            "batchId": batch_id,
            "retry": retry,
            "steps": steps,
        })
        if definition_snapshot is not UNSET:
            field_dict["definitionSnapshot"] = definition_snapshot
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if expected is not UNSET:
            field_dict["expected"] = expected

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_feedback import RunFeedback
        from ..models.workflow_run_execution_expected import WorkflowRunExecutionExpected
        d = dict(src_dict)
        status = ExecutionStatus(d.pop("status"))




        def _parse_schema_valid(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid"))


        def _parse_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        batch_id = _parse_batch_id(d.pop("batchId"))


        retry = RunExecutionRetry.from_dict(d.pop("retry"))




        steps = cast(list[Any], d.pop("steps"))


        def _parse_definition_snapshot(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        definition_snapshot = _parse_definition_snapshot(d.pop("definitionSnapshot", UNSET))


        def _parse_feedback(data: object) -> None | RunFeedback | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = RunFeedback.from_dict(data)



                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunFeedback | Unset, data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))


        _expected = d.pop("expected", UNSET)
        expected: WorkflowRunExecutionExpected | Unset
        if isinstance(_expected,  Unset):
            expected = UNSET
        else:
            expected = WorkflowRunExecutionExpected.from_dict(_expected)




        workflow_run_execution = cls(
            status=status,
            schema_valid=schema_valid,
            batch_id=batch_id,
            retry=retry,
            steps=steps,
            definition_snapshot=definition_snapshot,
            feedback=feedback,
            expected=expected,
        )

        return workflow_run_execution
