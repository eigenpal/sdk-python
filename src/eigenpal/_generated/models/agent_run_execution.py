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
  from ..models.agent_run_execution_expected import AgentRunExecutionExpected
  from ..models.agent_run_execution_files import AgentRunExecutionFiles
  from ..models.run_execution_retry import RunExecutionRetry
  from ..models.run_review import RunReview





T = TypeVar("T", bound="AgentRunExecution")



@_attrs_define
class AgentRunExecution:
    """
        Attributes:
            status (ExecutionStatus):
            schema_valid (bool | None): Whether the completed output matched the workflow or agent output schema.
            batch_id (None | str): Experiment batch id when the run is part of a batch.
            retry (RunExecutionRetry):
            files (AgentRunExecutionFiles):
            review (None | RunReview | Unset):
            expected (AgentRunExecutionExpected | Unset): Ground-truth expected output and files.
            comparison (Any | Unset): Expected-vs-actual comparison for eval runs (terminal runs only).
     """

    status: ExecutionStatus
    schema_valid: bool | None
    batch_id: None | str
    retry: RunExecutionRetry
    files: AgentRunExecutionFiles
    review: None | RunReview | Unset = UNSET
    expected: AgentRunExecutionExpected | Unset = UNSET
    comparison: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_execution_expected import AgentRunExecutionExpected
        from ..models.agent_run_execution_files import AgentRunExecutionFiles
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_review import RunReview
        status = self.status.value

        schema_valid: bool | None
        schema_valid = self.schema_valid

        batch_id: None | str
        batch_id = self.batch_id

        retry = self.retry.to_dict()

        files = self.files.to_dict()

        review: dict[str, Any] | None | Unset
        if isinstance(self.review, Unset):
            review = UNSET
        elif isinstance(self.review, RunReview):
            review = self.review.to_dict()
        else:
            review = self.review

        expected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected, Unset):
            expected = self.expected.to_dict()

        comparison = self.comparison


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "schemaValid": schema_valid,
            "batchId": batch_id,
            "retry": retry,
            "files": files,
        })
        if review is not UNSET:
            field_dict["review"] = review
        if expected is not UNSET:
            field_dict["expected"] = expected
        if comparison is not UNSET:
            field_dict["comparison"] = comparison

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_execution_expected import AgentRunExecutionExpected
        from ..models.agent_run_execution_files import AgentRunExecutionFiles
        from ..models.run_execution_retry import RunExecutionRetry
        from ..models.run_review import RunReview
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




        files = AgentRunExecutionFiles.from_dict(d.pop("files"))




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


        _expected = d.pop("expected", UNSET)
        expected: AgentRunExecutionExpected | Unset
        if isinstance(_expected,  Unset):
            expected = UNSET
        else:
            expected = AgentRunExecutionExpected.from_dict(_expected)




        comparison = d.pop("comparison", UNSET)

        agent_run_execution = cls(
            status=status,
            schema_valid=schema_valid,
            batch_id=batch_id,
            retry=retry,
            files=files,
            review=review,
            expected=expected,
            comparison=comparison,
        )

        return agent_run_execution
