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
  from ..models.agent_execution_summary_expected_files_item import AgentExecutionSummaryExpectedFilesItem
  from ..models.agent_execution_summary_feedback_type_0 import AgentExecutionSummaryFeedbackType0
  from ..models.agent_execution_summary_triggered_by_type_0 import AgentExecutionSummaryTriggeredByType0





T = TypeVar("T", bound="AgentExecutionSummary")



@_attrs_define
class AgentExecutionSummary:
    """ 
        Attributes:
            id (str):
            status (ExecutionStatus):
            created_at (str):
            trigger_type (None | str | Unset):
            triggered_by (AgentExecutionSummaryTriggeredByType0 | None | Unset):
            email_subject (None | str | Unset):
            email_from (None | str | Unset):
            model (None | str | Unset):
            output (Any | None | Unset):
            schema_valid (bool | None | Unset):
            error (None | str | Unset):
            requested_source_ref (None | str | Unset):
            resolved_git_ref (None | str | Unset):
            resolved_git_tag (None | str | Unset):
            resolved_commit_sha (None | str | Unset):
            example_id (None | str | Unset):
            batch_id (None | str | Unset):
            started_at (None | str | Unset):
            completed_at (None | str | Unset):
            feedback (AgentExecutionSummaryFeedbackType0 | None | Unset):
            expected (Any | None | Unset):
            expected_files (list[AgentExecutionSummaryExpectedFilesItem] | Unset):
     """

    id: str
    status: ExecutionStatus
    created_at: str
    trigger_type: None | str | Unset = UNSET
    triggered_by: AgentExecutionSummaryTriggeredByType0 | None | Unset = UNSET
    email_subject: None | str | Unset = UNSET
    email_from: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    output: Any | None | Unset = UNSET
    schema_valid: bool | None | Unset = UNSET
    error: None | str | Unset = UNSET
    requested_source_ref: None | str | Unset = UNSET
    resolved_git_ref: None | str | Unset = UNSET
    resolved_git_tag: None | str | Unset = UNSET
    resolved_commit_sha: None | str | Unset = UNSET
    example_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    feedback: AgentExecutionSummaryFeedbackType0 | None | Unset = UNSET
    expected: Any | None | Unset = UNSET
    expected_files: list[AgentExecutionSummaryExpectedFilesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_summary_expected_files_item import AgentExecutionSummaryExpectedFilesItem
        from ..models.agent_execution_summary_feedback_type_0 import AgentExecutionSummaryFeedbackType0
        from ..models.agent_execution_summary_triggered_by_type_0 import AgentExecutionSummaryTriggeredByType0
        id = self.id

        status = self.status.value

        created_at: str
        created_at = self.created_at

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = self.trigger_type

        triggered_by: dict[str, Any] | None | Unset
        if isinstance(self.triggered_by, Unset):
            triggered_by = UNSET
        elif isinstance(self.triggered_by, AgentExecutionSummaryTriggeredByType0):
            triggered_by = self.triggered_by.to_dict()
        else:
            triggered_by = self.triggered_by

        email_subject: None | str | Unset
        if isinstance(self.email_subject, Unset):
            email_subject = UNSET
        else:
            email_subject = self.email_subject

        email_from: None | str | Unset
        if isinstance(self.email_from, Unset):
            email_from = UNSET
        else:
            email_from = self.email_from

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        output: Any | None | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        schema_valid: bool | None | Unset
        if isinstance(self.schema_valid, Unset):
            schema_valid = UNSET
        else:
            schema_valid = self.schema_valid

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        requested_source_ref: None | str | Unset
        if isinstance(self.requested_source_ref, Unset):
            requested_source_ref = UNSET
        else:
            requested_source_ref = self.requested_source_ref

        resolved_git_ref: None | str | Unset
        if isinstance(self.resolved_git_ref, Unset):
            resolved_git_ref = UNSET
        else:
            resolved_git_ref = self.resolved_git_ref

        resolved_git_tag: None | str | Unset
        if isinstance(self.resolved_git_tag, Unset):
            resolved_git_tag = UNSET
        else:
            resolved_git_tag = self.resolved_git_tag

        resolved_commit_sha: None | str | Unset
        if isinstance(self.resolved_commit_sha, Unset):
            resolved_commit_sha = UNSET
        else:
            resolved_commit_sha = self.resolved_commit_sha

        example_id: None | str | Unset
        if isinstance(self.example_id, Unset):
            example_id = UNSET
        else:
            example_id = self.example_id

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

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

        feedback: dict[str, Any] | None | Unset
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        elif isinstance(self.feedback, AgentExecutionSummaryFeedbackType0):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        expected: Any | None | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        expected_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expected_files, Unset):
            expected_files = []
            for expected_files_item_data in self.expected_files:
                expected_files_item = expected_files_item_data.to_dict()
                expected_files.append(expected_files_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
            "createdAt": created_at,
        })
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type
        if triggered_by is not UNSET:
            field_dict["triggeredBy"] = triggered_by
        if email_subject is not UNSET:
            field_dict["emailSubject"] = email_subject
        if email_from is not UNSET:
            field_dict["emailFrom"] = email_from
        if model is not UNSET:
            field_dict["model"] = model
        if output is not UNSET:
            field_dict["output"] = output
        if schema_valid is not UNSET:
            field_dict["schemaValid"] = schema_valid
        if error is not UNSET:
            field_dict["error"] = error
        if requested_source_ref is not UNSET:
            field_dict["requestedSourceRef"] = requested_source_ref
        if resolved_git_ref is not UNSET:
            field_dict["resolvedGitRef"] = resolved_git_ref
        if resolved_git_tag is not UNSET:
            field_dict["resolvedGitTag"] = resolved_git_tag
        if resolved_commit_sha is not UNSET:
            field_dict["resolvedCommitSha"] = resolved_commit_sha
        if example_id is not UNSET:
            field_dict["exampleId"] = example_id
        if batch_id is not UNSET:
            field_dict["batchId"] = batch_id
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if expected is not UNSET:
            field_dict["expected"] = expected
        if expected_files is not UNSET:
            field_dict["expectedFiles"] = expected_files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_summary_expected_files_item import AgentExecutionSummaryExpectedFilesItem
        from ..models.agent_execution_summary_feedback_type_0 import AgentExecutionSummaryFeedbackType0
        from ..models.agent_execution_summary_triggered_by_type_0 import AgentExecutionSummaryTriggeredByType0
        d = dict(src_dict)
        id = d.pop("id")

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


        def _parse_triggered_by(data: object) -> AgentExecutionSummaryTriggeredByType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                triggered_by_type_0 = AgentExecutionSummaryTriggeredByType0.from_dict(data)



                return triggered_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionSummaryTriggeredByType0 | None | Unset, data)

        triggered_by = _parse_triggered_by(d.pop("triggeredBy", UNSET))


        def _parse_email_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_subject = _parse_email_subject(d.pop("emailSubject", UNSET))


        def _parse_email_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_from = _parse_email_from(d.pop("emailFrom", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_output(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        output = _parse_output(d.pop("output", UNSET))


        def _parse_schema_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_requested_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_source_ref = _parse_requested_source_ref(d.pop("requestedSourceRef", UNSET))


        def _parse_resolved_git_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_git_ref = _parse_resolved_git_ref(d.pop("resolvedGitRef", UNSET))


        def _parse_resolved_git_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_git_tag = _parse_resolved_git_tag(d.pop("resolvedGitTag", UNSET))


        def _parse_resolved_commit_sha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_commit_sha = _parse_resolved_commit_sha(d.pop("resolvedCommitSha", UNSET))


        def _parse_example_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example_id = _parse_example_id(d.pop("exampleId", UNSET))


        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batchId", UNSET))


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


        def _parse_feedback(data: object) -> AgentExecutionSummaryFeedbackType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = AgentExecutionSummaryFeedbackType0.from_dict(data)



                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionSummaryFeedbackType0 | None | Unset, data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))


        def _parse_expected(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        _expected_files = d.pop("expectedFiles", UNSET)
        expected_files: list[AgentExecutionSummaryExpectedFilesItem] | Unset = UNSET
        if _expected_files is not UNSET:
            expected_files = []
            for expected_files_item_data in _expected_files:
                expected_files_item = AgentExecutionSummaryExpectedFilesItem.from_dict(expected_files_item_data)



                expected_files.append(expected_files_item)


        agent_execution_summary = cls(
            id=id,
            status=status,
            created_at=created_at,
            trigger_type=trigger_type,
            triggered_by=triggered_by,
            email_subject=email_subject,
            email_from=email_from,
            model=model,
            output=output,
            schema_valid=schema_valid,
            error=error,
            requested_source_ref=requested_source_ref,
            resolved_git_ref=resolved_git_ref,
            resolved_git_tag=resolved_git_tag,
            resolved_commit_sha=resolved_commit_sha,
            example_id=example_id,
            batch_id=batch_id,
            started_at=started_at,
            completed_at=completed_at,
            feedback=feedback,
            expected=expected,
            expected_files=expected_files,
        )


        agent_execution_summary.additional_properties = d
        return agent_execution_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
