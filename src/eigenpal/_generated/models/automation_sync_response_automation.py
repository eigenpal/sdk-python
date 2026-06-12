from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_sync_response_automation_status import AutomationSyncResponseAutomationStatus
from ..models.automation_sync_response_automation_type import AutomationSyncResponseAutomationType






T = TypeVar("T", bound="AutomationSyncResponseAutomation")



@_attrs_define
class AutomationSyncResponseAutomation:
    """
        Attributes:
            id (str):
            type_ (AutomationSyncResponseAutomationType):
            slug (str):
            status (AutomationSyncResponseAutomationStatus):
            updated_at (str):
     """

    id: str
    type_: AutomationSyncResponseAutomationType
    slug: str
    status: AutomationSyncResponseAutomationStatus
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        slug = self.slug

        status = self.status.value

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "slug": slug,
            "status": status,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = AutomationSyncResponseAutomationType(d.pop("type"))




        slug = d.pop("slug")

        status = AutomationSyncResponseAutomationStatus(d.pop("status"))




        updated_at = d.pop("updatedAt")

        automation_sync_response_automation = cls(
            id=id,
            type_=type_,
            slug=slug,
            status=status,
            updated_at=updated_at,
        )

        return automation_sync_response_automation
