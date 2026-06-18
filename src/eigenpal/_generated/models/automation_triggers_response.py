from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_type import AutomationType
from typing import cast

if TYPE_CHECKING:
  from ..models.automation_trigger_state import AutomationTriggerState





T = TypeVar("T", bound="AutomationTriggersResponse")



@_attrs_define
class AutomationTriggersResponse:
    """
        Attributes:
            automation_id (str):
            type_ (AutomationType):
            triggers (AutomationTriggerState):
     """

    automation_id: str
    type_: AutomationType
    triggers: AutomationTriggerState





    def to_dict(self) -> dict[str, Any]:
        from ..models.automation_trigger_state import AutomationTriggerState
        automation_id = self.automation_id

        type_ = self.type_.value

        triggers = self.triggers.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "automationId": automation_id,
            "type": type_,
            "triggers": triggers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_trigger_state import AutomationTriggerState
        d = dict(src_dict)
        automation_id = d.pop("automationId")

        type_ = AutomationType(d.pop("type"))




        triggers = AutomationTriggerState.from_dict(d.pop("triggers"))




        automation_triggers_response = cls(
            automation_id=automation_id,
            type_=type_,
            triggers=triggers,
        )

        return automation_triggers_response
