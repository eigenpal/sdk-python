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
  from ..models.run_review import RunReview
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
            review (None | RunReview | Unset):
            definition_snapshot (Any | None | Unset): Workflow definition snapshot captured when the run was created.
            expected (WorkflowRunExecutionExpected | Unset): Ground-truth expected output and files.
     """

    status: ExecutionStatus
    schema_valid: bool | None
    batch_id: None | str
    retry: RunExecutionRetry
    steps: list[Any]
    review: None | RunReview | Unset = UNSET
    definition_snapshot: Any | None | Unset = UNSET
    expected: WorkflowRunExecutionExpected | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_review import RunReview
        from ..models.workflow_run_execution_expected import WorkflowRunExecutionExpected
        status = self.status.value

        schema_valid: bool | None
        schema_valid = self.schema_valid

        batch_id: None | str
        batch_id = self.batch_id

        retry = self.retry.to_dict()

        steps = self.steps



        review: dict[str, Any] | None | Unset
        if isinstance(self.review, Unset):
            review = UNSET
        elif isinstance(self.review, RunReview):
            review = self.review.to_dict()
        else:
            review = self.review

        definition_snapshot: Any | None | Unset
        if isinstance(self.definition_snapshot, Unset):
            definition_snapshot = UNSET
        else:
            definition_snapshot = self.definition_snapshot

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
        if review is not UNSET:
            field_dict["review"] = review
        if definition_snapshot is not UNSET:
            field_dict["definitionSnapshot"] = definition_snapshot
        if expected is not UNSET:
            field_dict["expected"] = expected

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_review import RunReview
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


        def _parse_review(data: object) -> None | RunReview | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                review_type_0 = RunReview.from_dict(data)



                return review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunReview | Unset, data)

        review = _parse_review(d.pop("review", UNSET))


        def _parse_definition_snapshot(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        definition_snapshot = _parse_definition_snapshot(d.pop("definitionSnapshot", UNSET))


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
            review=review,
            definition_snapshot=definition_snapshot,
            expected=expected,
        )

        return workflow_run_execution
