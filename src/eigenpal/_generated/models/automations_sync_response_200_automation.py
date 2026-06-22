from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automations_sync_response_200_automation_status import AutomationsSyncResponse200AutomationStatus
from ..models.automations_sync_response_200_automation_type import AutomationsSyncResponse200AutomationType






T = TypeVar("T", bound="AutomationsSyncResponse200Automation")



@_attrs_define
class AutomationsSyncResponse200Automation:
    """
        Attributes:
            id (str): Automation id after reconciliation.
            type_ (AutomationsSyncResponse200AutomationType): Automation kind inferred from the source package path.
            slug (str): Source package slug within agents/ or workflows/.
            status (AutomationsSyncResponse200AutomationStatus): Current automation registry status.
            updated_at (str): ISO timestamp for the reconciled automation row.
     """

    id: str
    type_: AutomationsSyncResponse200AutomationType
    slug: str
    status: AutomationsSyncResponse200AutomationStatus
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

        type_ = AutomationsSyncResponse200AutomationType(d.pop("type"))




        slug = d.pop("slug")

        status = AutomationsSyncResponse200AutomationStatus(d.pop("status"))




        updated_at = d.pop("updatedAt")

        automations_sync_response_200_automation = cls(
            id=id,
            type_=type_,
            slug=slug,
            status=status,
            updated_at=updated_at,
        )

        return automations_sync_response_200_automation
