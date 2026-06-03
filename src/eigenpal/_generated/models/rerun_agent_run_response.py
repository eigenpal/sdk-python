from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RerunAgentRunResponse")



@_attrs_define
class RerunAgentRunResponse:
    """ 
        Attributes:
            run_id (str):
            source_run_id (str):
            status (ExecutionStatus):
            requested_source_ref (None | str | Unset):
            resolved_git_ref (None | str | Unset):
            resolved_git_tag (None | str | Unset):
            resolved_commit_sha (None | str | Unset):
     """

    run_id: str
    source_run_id: str
    status: ExecutionStatus
    requested_source_ref: None | str | Unset = UNSET
    resolved_git_ref: None | str | Unset = UNSET
    resolved_git_tag: None | str | Unset = UNSET
    resolved_commit_sha: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        source_run_id = self.source_run_id

        status = self.status.value

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runId": run_id,
            "sourceRunId": source_run_id,
            "status": status,
        })
        if requested_source_ref is not UNSET:
            field_dict["requestedSourceRef"] = requested_source_ref
        if resolved_git_ref is not UNSET:
            field_dict["resolvedGitRef"] = resolved_git_ref
        if resolved_git_tag is not UNSET:
            field_dict["resolvedGitTag"] = resolved_git_tag
        if resolved_commit_sha is not UNSET:
            field_dict["resolvedCommitSha"] = resolved_commit_sha

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        source_run_id = d.pop("sourceRunId")

        status = ExecutionStatus(d.pop("status"))




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


        rerun_agent_run_response = cls(
            run_id=run_id,
            source_run_id=source_run_id,
            status=status,
            requested_source_ref=requested_source_ref,
            resolved_git_ref=resolved_git_ref,
            resolved_git_tag=resolved_git_tag,
            resolved_commit_sha=resolved_commit_sha,
        )

        return rerun_agent_run_response

