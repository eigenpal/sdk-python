from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AutomationVersion")



@_attrs_define
class AutomationVersion:
    """
        Attributes:
            id (str):
            automation_id (str):
            version (None | str):
            source_ref (None | str | Unset):
            is_current (bool | Unset):
            created_at (str | Unset):
     """

    id: str
    automation_id: str
    version: None | str
    source_ref: None | str | Unset = UNSET
    is_current: bool | Unset = UNSET
    created_at: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        automation_id = self.automation_id

        version: None | str
        version = self.version

        source_ref: None | str | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = self.source_ref

        is_current = self.is_current

        created_at: str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "automationId": automation_id,
            "version": version,
        })
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        automation_id = d.pop("automationId")

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))


        def _parse_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_ref = _parse_source_ref(d.pop("sourceRef", UNSET))


        is_current = d.pop("isCurrent", UNSET)

        def _parse_created_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        automation_version = cls(
            id=id,
            automation_id=automation_id,
            version=version,
            source_ref=source_ref,
            is_current=is_current,
            created_at=created_at,
        )

        return automation_version
