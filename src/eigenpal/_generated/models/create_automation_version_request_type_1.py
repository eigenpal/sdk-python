from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateAutomationVersionRequestType1")



@_attrs_define
class CreateAutomationVersionRequestType1:
    """
        Attributes:
            history_id (str): Existing version id from GET /automations/{id}/versions. Creates a new tagged snapshot copied
                from that version; the source tag is left unchanged. Mutually exclusive with `yaml`.
            version (str): Bare semver tag such as 1.2.0. Do not include a leading v.
            activate (bool | Unset): Whether to make the new version current immediately. Defaults to true. Set false to
                keep a tagged candidate off live traffic until promote. `activate: false` requires an existing current workflow
                version and returns 400 if HEAD is empty.
     """

    history_id: str
    version: str
    activate: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        version = self.version

        activate = self.activate


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "historyId": history_id,
            "version": version,
        })
        if activate is not UNSET:
            field_dict["activate"] = activate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        history_id = d.pop("historyId")

        version = d.pop("version")

        activate = d.pop("activate", UNSET)

        create_automation_version_request_type_1 = cls(
            history_id=history_id,
            version=version,
            activate=activate,
        )

        return create_automation_version_request_type_1
