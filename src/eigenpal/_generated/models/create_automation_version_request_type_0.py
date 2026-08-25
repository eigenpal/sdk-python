from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateAutomationVersionRequestType0")



@_attrs_define
class CreateAutomationVersionRequestType0:
    """
        Attributes:
            yaml (str): Validated workflow YAML to publish as a new tagged version. Mutually exclusive with `historyId`. At
                most 1 MiB.
            version (str): Bare semver tag such as 1.2.0. Do not include a leading v.
            activate (bool | Unset): Whether to make the new version current immediately. Defaults to true. Set false to
                keep a tagged candidate off live traffic until promote. `activate: false` requires an existing current workflow
                version and returns 400 if HEAD is empty.
     """

    yaml: str
    version: str
    activate: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        yaml = self.yaml

        version = self.version

        activate = self.activate


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "yaml": yaml,
            "version": version,
        })
        if activate is not UNSET:
            field_dict["activate"] = activate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        yaml = d.pop("yaml")

        version = d.pop("version")

        activate = d.pop("activate", UNSET)

        create_automation_version_request_type_0 = cls(
            yaml=yaml,
            version=version,
            activate=activate,
        )

        return create_automation_version_request_type_0
