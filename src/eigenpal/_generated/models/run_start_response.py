from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..models.run_start_response_type import RunStartResponseType
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.run_start_response_cost import RunStartResponseCost





T = TypeVar("T", bound="RunStartResponse")



@_attrs_define
class RunStartResponse:
    """ 
        Attributes:
            run_id (str):
            type_ (RunStartResponseType):
            status (ExecutionStatus | Literal['pending'] | Literal['timeout'] | Unset):
            output (Any | Unset):
            error (None | str | Unset):
            schema_valid (bool | None | Unset):
            requested_source_ref (None | str | Unset):
            resolved_git_ref (None | str | Unset):
            resolved_git_tag (None | str | Unset):
            resolved_commit_sha (None | str | Unset):
            cost (RunStartResponseCost | Unset):
     """

    run_id: str
    type_: RunStartResponseType
    status: ExecutionStatus | Literal['pending'] | Literal['timeout'] | Unset = UNSET
    output: Any | Unset = UNSET
    error: None | str | Unset = UNSET
    schema_valid: bool | None | Unset = UNSET
    requested_source_ref: None | str | Unset = UNSET
    resolved_git_ref: None | str | Unset = UNSET
    resolved_git_tag: None | str | Unset = UNSET
    resolved_commit_sha: None | str | Unset = UNSET
    cost: RunStartResponseCost | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_response_cost import RunStartResponseCost
        run_id = self.run_id

        type_ = self.type_.value

        status: Literal['pending'] | Literal['timeout'] | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ExecutionStatus):
            status = self.status.value
        else:
            status = self.status

        output = self.output

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        schema_valid: bool | None | Unset
        if isinstance(self.schema_valid, Unset):
            schema_valid = UNSET
        else:
            schema_valid = self.schema_valid

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

        cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runId": run_id,
            "type": type_,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if schema_valid is not UNSET:
            field_dict["schemaValid"] = schema_valid
        if requested_source_ref is not UNSET:
            field_dict["requestedSourceRef"] = requested_source_ref
        if resolved_git_ref is not UNSET:
            field_dict["resolvedGitRef"] = resolved_git_ref
        if resolved_git_tag is not UNSET:
            field_dict["resolvedGitTag"] = resolved_git_tag
        if resolved_commit_sha is not UNSET:
            field_dict["resolvedCommitSha"] = resolved_commit_sha
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_response_cost import RunStartResponseCost
        d = dict(src_dict)
        run_id = d.pop("runId")

        type_ = RunStartResponseType(d.pop("type"))




        def _parse_status(data: object) -> ExecutionStatus | Literal['pending'] | Literal['timeout'] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0_type_0 = ExecutionStatus(data)



                return status_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            status_type_0_type_1 = cast(Literal['pending'] , data)
            if status_type_0_type_1 != 'pending':
                raise ValueError(f"status_type_0_type_1 must match const 'pending', got '{status_type_0_type_1}'")
            return status_type_0_type_1
            status_type_1 = cast(Literal['timeout'] , data)
            if status_type_1 != 'timeout':
                raise ValueError(f"status_type_1 must match const 'timeout', got '{status_type_1}'")
            return status_type_1

        status = _parse_status(d.pop("status", UNSET))


        output = d.pop("output", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_schema_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid", UNSET))


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


        _cost = d.pop("cost", UNSET)
        cost: RunStartResponseCost | Unset
        if isinstance(_cost,  Unset):
            cost = UNSET
        else:
            cost = RunStartResponseCost.from_dict(_cost)




        run_start_response = cls(
            run_id=run_id,
            type_=type_,
            status=status,
            output=output,
            error=error,
            schema_valid=schema_valid,
            requested_source_ref=requested_source_ref,
            resolved_git_ref=resolved_git_ref,
            resolved_git_tag=resolved_git_tag,
            resolved_commit_sha=resolved_commit_sha,
            cost=cost,
        )

        return run_start_response

