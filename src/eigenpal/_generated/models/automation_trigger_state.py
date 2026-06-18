from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AutomationTriggerState")



@_attrs_define
class AutomationTriggerState:
    """
        Attributes:
            api (bool):
            email (bool):
            manual (bool):
            cron (bool):
     """

    api: bool
    email: bool
    manual: bool
    cron: bool





    def to_dict(self) -> dict[str, Any]:
        api = self.api

        email = self.email

        manual = self.manual

        cron = self.cron


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "api": api,
            "email": email,
            "manual": manual,
            "cron": cron,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api = d.pop("api")

        email = d.pop("email")

        manual = d.pop("manual")

        cron = d.pop("cron")

        automation_trigger_state = cls(
            api=api,
            email=email,
            manual=manual,
            cron=cron,
        )

        return automation_trigger_state
