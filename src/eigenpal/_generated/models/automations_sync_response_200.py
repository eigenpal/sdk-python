from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.automations_sync_response_200_automation import AutomationsSyncResponse200Automation
  from ..models.automations_sync_response_200_release import AutomationsSyncResponse200Release





T = TypeVar("T", bound="AutomationsSyncResponse200")



@_attrs_define
class AutomationsSyncResponse200:
    """
        Attributes:
            automation (AutomationsSyncResponse200Automation):
            release (AutomationsSyncResponse200Release):
            warnings (list[str]): Non-fatal source-state warnings, such as unsupported email alias domains.
     """

    automation: AutomationsSyncResponse200Automation
    release: AutomationsSyncResponse200Release
    warnings: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.automations_sync_response_200_automation import AutomationsSyncResponse200Automation
        from ..models.automations_sync_response_200_release import AutomationsSyncResponse200Release
        automation = self.automation.to_dict()

        release = self.release.to_dict()

        warnings = self.warnings




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "automation": automation,
            "release": release,
            "warnings": warnings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_sync_response_200_automation import AutomationsSyncResponse200Automation
        from ..models.automations_sync_response_200_release import AutomationsSyncResponse200Release
        d = dict(src_dict)
        automation = AutomationsSyncResponse200Automation.from_dict(d.pop("automation"))




        release = AutomationsSyncResponse200Release.from_dict(d.pop("release"))




        warnings = cast(list[str], d.pop("warnings"))


        automations_sync_response_200 = cls(
            automation=automation,
            release=release,
            warnings=warnings,
        )

        return automations_sync_response_200
