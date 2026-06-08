from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_summary_status import RunSummaryStatus
from ..models.run_summary_type import RunSummaryType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_summary_triggered_by_type_0 import RunSummaryTriggeredByType0





T = TypeVar("T", bound="RunSummary")



@_attrs_define
class RunSummary:
    """ 
        Attributes:
            id (str):
            type_ (RunSummaryType):
            status (RunSummaryStatus):
            trigger_type (None | str):
            created_at (str):
            duration_ms (float | None):
            error (None | str):
            batch_id (None | str):
            previous_execution_id (None | str):
            retry_number (float):
            schema_valid (bool | None):
            eval_passed (bool | None):
            triggered_by (None | RunSummaryTriggeredByType0):
            version (None | str):
            requested_source_ref (None | str):
            resolved_git_ref (None | str):
            resolved_git_tag (None | str):
            resolved_commit_sha (None | str):
            source_id (str):
            source_name (None | str):
            agent_slug (None | str):
            started_at (None | str | Unset):
            completed_at (None | str | Unset):
            eval_score (float | None | Unset):
            example_id (None | str | Unset):
            example_name (None | str | Unset):
     """

    id: str
    type_: RunSummaryType
    status: RunSummaryStatus
    trigger_type: None | str
    created_at: str
    duration_ms: float | None
    error: None | str
    batch_id: None | str
    previous_execution_id: None | str
    retry_number: float
    schema_valid: bool | None
    eval_passed: bool | None
    triggered_by: None | RunSummaryTriggeredByType0
    version: None | str
    requested_source_ref: None | str
    resolved_git_ref: None | str
    resolved_git_tag: None | str
    resolved_commit_sha: None | str
    source_id: str
    source_name: None | str
    agent_slug: None | str
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    eval_score: float | None | Unset = UNSET
    example_id: None | str | Unset = UNSET
    example_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_summary_triggered_by_type_0 import RunSummaryTriggeredByType0
        id = self.id

        type_ = self.type_.value

        status = self.status.value

        trigger_type: None | str
        trigger_type = self.trigger_type

        created_at = self.created_at

        duration_ms: float | None
        duration_ms = self.duration_ms

        error: None | str
        error = self.error

        batch_id: None | str
        batch_id = self.batch_id

        previous_execution_id: None | str
        previous_execution_id = self.previous_execution_id

        retry_number = self.retry_number

        schema_valid: bool | None
        schema_valid = self.schema_valid

        eval_passed: bool | None
        eval_passed = self.eval_passed

        triggered_by: dict[str, Any] | None
        if isinstance(self.triggered_by, RunSummaryTriggeredByType0):
            triggered_by = self.triggered_by.to_dict()
        else:
            triggered_by = self.triggered_by

        version: None | str
        version = self.version

        requested_source_ref: None | str
        requested_source_ref = self.requested_source_ref

        resolved_git_ref: None | str
        resolved_git_ref = self.resolved_git_ref

        resolved_git_tag: None | str
        resolved_git_tag = self.resolved_git_tag

        resolved_commit_sha: None | str
        resolved_commit_sha = self.resolved_commit_sha

        source_id = self.source_id

        source_name: None | str
        source_name = self.source_name

        agent_slug: None | str
        agent_slug = self.agent_slug

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

        eval_score: float | None | Unset
        if isinstance(self.eval_score, Unset):
            eval_score = UNSET
        else:
            eval_score = self.eval_score

        example_id: None | str | Unset
        if isinstance(self.example_id, Unset):
            example_id = UNSET
        else:
            example_id = self.example_id

        example_name: None | str | Unset
        if isinstance(self.example_name, Unset):
            example_name = UNSET
        else:
            example_name = self.example_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "status": status,
            "triggerType": trigger_type,
            "createdAt": created_at,
            "durationMs": duration_ms,
            "error": error,
            "batchId": batch_id,
            "previousExecutionId": previous_execution_id,
            "retryNumber": retry_number,
            "schemaValid": schema_valid,
            "evalPassed": eval_passed,
            "triggeredBy": triggered_by,
            "version": version,
            "requestedSourceRef": requested_source_ref,
            "resolvedGitRef": resolved_git_ref,
            "resolvedGitTag": resolved_git_tag,
            "resolvedCommitSha": resolved_commit_sha,
            "sourceId": source_id,
            "sourceName": source_name,
            "agentSlug": agent_slug,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if eval_score is not UNSET:
            field_dict["evalScore"] = eval_score
        if example_id is not UNSET:
            field_dict["exampleId"] = example_id
        if example_name is not UNSET:
            field_dict["exampleName"] = example_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_summary_triggered_by_type_0 import RunSummaryTriggeredByType0
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RunSummaryType(d.pop("type"))




        status = RunSummaryStatus(d.pop("status"))




        def _parse_trigger_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trigger_type = _parse_trigger_type(d.pop("triggerType"))


        created_at = d.pop("createdAt")

        def _parse_duration_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs"))


        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))


        def _parse_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        batch_id = _parse_batch_id(d.pop("batchId"))


        def _parse_previous_execution_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_execution_id = _parse_previous_execution_id(d.pop("previousExecutionId"))


        retry_number = d.pop("retryNumber")

        def _parse_schema_valid(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid"))


        def _parse_eval_passed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        eval_passed = _parse_eval_passed(d.pop("evalPassed"))


        def _parse_triggered_by(data: object) -> None | RunSummaryTriggeredByType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                triggered_by_type_0 = RunSummaryTriggeredByType0.from_dict(data)



                return triggered_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunSummaryTriggeredByType0, data)

        triggered_by = _parse_triggered_by(d.pop("triggeredBy"))


        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))


        def _parse_requested_source_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        requested_source_ref = _parse_requested_source_ref(d.pop("requestedSourceRef"))


        def _parse_resolved_git_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_git_ref = _parse_resolved_git_ref(d.pop("resolvedGitRef"))


        def _parse_resolved_git_tag(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_git_tag = _parse_resolved_git_tag(d.pop("resolvedGitTag"))


        def _parse_resolved_commit_sha(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_commit_sha = _parse_resolved_commit_sha(d.pop("resolvedCommitSha"))


        source_id = d.pop("sourceId")

        def _parse_source_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_name = _parse_source_name(d.pop("sourceName"))


        def _parse_agent_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_slug = _parse_agent_slug(d.pop("agentSlug"))


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


        def _parse_eval_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        eval_score = _parse_eval_score(d.pop("evalScore", UNSET))


        def _parse_example_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example_id = _parse_example_id(d.pop("exampleId", UNSET))


        def _parse_example_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example_name = _parse_example_name(d.pop("exampleName", UNSET))


        run_summary = cls(
            id=id,
            type_=type_,
            status=status,
            trigger_type=trigger_type,
            created_at=created_at,
            duration_ms=duration_ms,
            error=error,
            batch_id=batch_id,
            previous_execution_id=previous_execution_id,
            retry_number=retry_number,
            schema_valid=schema_valid,
            eval_passed=eval_passed,
            triggered_by=triggered_by,
            version=version,
            requested_source_ref=requested_source_ref,
            resolved_git_ref=resolved_git_ref,
            resolved_git_tag=resolved_git_tag,
            resolved_commit_sha=resolved_commit_sha,
            source_id=source_id,
            source_name=source_name,
            agent_slug=agent_slug,
            started_at=started_at,
            completed_at=completed_at,
            eval_score=eval_score,
            example_id=example_id,
            example_name=example_name,
        )

        return run_summary

