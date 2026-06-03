from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListAgentVersionsResponseVersionsItem")



@_attrs_define
class ListAgentVersionsResponseVersionsItem:
    """ 
        Attributes:
            version (str):
            source_ref (str):
            tag (str):
            commit (str):
            notes (None | str):
            created_at (None | str):
            latest (bool):
     """

    version: str
    source_ref: str
    tag: str
    commit: str
    notes: None | str
    created_at: None | str
    latest: bool





    def to_dict(self) -> dict[str, Any]:
        version = self.version

        source_ref = self.source_ref

        tag = self.tag

        commit = self.commit

        notes: None | str
        notes = self.notes

        created_at: None | str
        created_at = self.created_at

        latest = self.latest


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "version": version,
            "sourceRef": source_ref,
            "tag": tag,
            "commit": commit,
            "notes": notes,
            "createdAt": created_at,
            "latest": latest,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        source_ref = d.pop("sourceRef")

        tag = d.pop("tag")

        commit = d.pop("commit")

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))


        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        latest = d.pop("latest")

        list_agent_versions_response_versions_item = cls(
            version=version,
            source_ref=source_ref,
            tag=tag,
            commit=commit,
            notes=notes,
            created_at=created_at,
            latest=latest,
        )

        return list_agent_versions_response_versions_item

