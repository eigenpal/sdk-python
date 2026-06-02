from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.automation_sync_response_automation import AutomationSyncResponseAutomation
  from ..models.automation_sync_response_release import AutomationSyncResponseRelease





T = TypeVar("T", bound="AutomationSyncResponse")



@_attrs_define
class AutomationSyncResponse:
    """ 
        Attributes:
            automation (AutomationSyncResponseAutomation):
            release (AutomationSyncResponseRelease):
            warnings (list[str]):
     """

    automation: AutomationSyncResponseAutomation
    release: AutomationSyncResponseRelease
    warnings: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.automation_sync_response_automation import AutomationSyncResponseAutomation
        from ..models.automation_sync_response_release import AutomationSyncResponseRelease
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
        from ..models.automation_sync_response_automation import AutomationSyncResponseAutomation
        from ..models.automation_sync_response_release import AutomationSyncResponseRelease
        d = dict(src_dict)
        automation = AutomationSyncResponseAutomation.from_dict(d.pop("automation"))




        release = AutomationSyncResponseRelease.from_dict(d.pop("release"))




        warnings = cast(list[str], d.pop("warnings"))


        automation_sync_response = cls(
            automation=automation,
            release=release,
            warnings=warnings,
        )

        return automation_sync_response

