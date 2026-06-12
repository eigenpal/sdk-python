from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AutomationSyncResponseRelease")



@_attrs_define
class AutomationSyncResponseRelease:
    """
        Attributes:
            version (str):
            tag (str):
            commit (str):
     """

    version: str
    tag: str
    commit: str





    def to_dict(self) -> dict[str, Any]:
        version = self.version

        tag = self.tag

        commit = self.commit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "version": version,
            "tag": tag,
            "commit": commit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        tag = d.pop("tag")

        commit = d.pop("commit")

        automation_sync_response_release = cls(
            version=version,
            tag=tag,
            commit=commit,
        )

        return automation_sync_response_release
