from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunSourceGit")



@_attrs_define
class RunSourceGit:
    """
        Attributes:
            requested_ref (None | str):
            resolved_ref (None | str):
            resolved_tag (None | str):
            commit_sha (None | str):
     """

    requested_ref: None | str
    resolved_ref: None | str
    resolved_tag: None | str
    commit_sha: None | str





    def to_dict(self) -> dict[str, Any]:
        requested_ref: None | str
        requested_ref = self.requested_ref

        resolved_ref: None | str
        resolved_ref = self.resolved_ref

        resolved_tag: None | str
        resolved_tag = self.resolved_tag

        commit_sha: None | str
        commit_sha = self.commit_sha


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "requestedRef": requested_ref,
            "resolvedRef": resolved_ref,
            "resolvedTag": resolved_tag,
            "commitSha": commit_sha,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_requested_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        requested_ref = _parse_requested_ref(d.pop("requestedRef"))


        def _parse_resolved_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_ref = _parse_resolved_ref(d.pop("resolvedRef"))


        def _parse_resolved_tag(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_tag = _parse_resolved_tag(d.pop("resolvedTag"))


        def _parse_commit_sha(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_sha = _parse_commit_sha(d.pop("commitSha"))


        run_source_git = cls(
            requested_ref=requested_ref,
            resolved_ref=resolved_ref,
            resolved_tag=resolved_tag,
            commit_sha=commit_sha,
        )

        return run_source_git
