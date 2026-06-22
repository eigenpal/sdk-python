from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AutomationsSyncResponse200Release")



@_attrs_define
class AutomationsSyncResponse200Release:
    """
        Attributes:
            version (str): Latest released source package version that was synced.
            tag (str): Git release tag read during sync.
            commit (str): Git commit for the release tag.
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

        automations_sync_response_200_release = cls(
            version=version,
            tag=tag,
            commit=commit,
        )

        return automations_sync_response_200_release
