from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_versions_response_versions_item_created_by_user_type_0 import ListAgentVersionsResponseVersionsItemCreatedByUserType0





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
            created_by_user (ListAgentVersionsResponseVersionsItemCreatedByUserType0 | None):
            latest (bool):
     """

    version: str
    source_ref: str
    tag: str
    commit: str
    notes: None | str
    created_at: None | str
    created_by_user: ListAgentVersionsResponseVersionsItemCreatedByUserType0 | None
    latest: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_versions_response_versions_item_created_by_user_type_0 import ListAgentVersionsResponseVersionsItemCreatedByUserType0
        version = self.version

        source_ref = self.source_ref

        tag = self.tag

        commit = self.commit

        notes: None | str
        notes = self.notes

        created_at: None | str
        created_at = self.created_at

        created_by_user: dict[str, Any] | None
        if isinstance(self.created_by_user, ListAgentVersionsResponseVersionsItemCreatedByUserType0):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        latest = self.latest


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "version": version,
            "sourceRef": source_ref,
            "tag": tag,
            "commit": commit,
            "notes": notes,
            "createdAt": created_at,
            "createdByUser": created_by_user,
            "latest": latest,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_versions_response_versions_item_created_by_user_type_0 import ListAgentVersionsResponseVersionsItemCreatedByUserType0
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


        def _parse_created_by_user(data: object) -> ListAgentVersionsResponseVersionsItemCreatedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = ListAgentVersionsResponseVersionsItemCreatedByUserType0.from_dict(data)



                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentVersionsResponseVersionsItemCreatedByUserType0 | None, data)

        created_by_user = _parse_created_by_user(d.pop("createdByUser"))


        latest = d.pop("latest")

        list_agent_versions_response_versions_item = cls(
            version=version,
            source_ref=source_ref,
            tag=tag,
            commit=commit,
            notes=notes,
            created_at=created_at,
            created_by_user=created_by_user,
            latest=latest,
        )

        return list_agent_versions_response_versions_item
