from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentsTriggersEmailUpdateResponse200")



@_attrs_define
class AgentsTriggersEmailUpdateResponse200:
    """
        Attributes:
            trigger (Any):
     """

    trigger: Any





    def to_dict(self) -> dict[str, Any]:
        trigger = self.trigger


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "trigger": trigger,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger = d.pop("trigger")

        agents_triggers_email_update_response_200 = cls(
            trigger=trigger,
        )

        return agents_triggers_email_update_response_200
