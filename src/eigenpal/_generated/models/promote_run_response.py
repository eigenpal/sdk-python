from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promote_run_response_automation_type import PromoteRunResponseAutomationType
from typing import cast






T = TypeVar("T", bound="PromoteRunResponse")



@_attrs_define
class PromoteRunResponse:
    """
        Attributes:
            automation_id (str): Automation that owns the promoted example.
            automation_type (PromoteRunResponseAutomationType): Implementation type behind the automation.
            example_id (str): Dataset example identifier returned for follow-up API calls.
            name (None | str): Dataset example name.
     """

    automation_id: str
    automation_type: PromoteRunResponseAutomationType
    example_id: str
    name: None | str





    def to_dict(self) -> dict[str, Any]:
        automation_id = self.automation_id

        automation_type = self.automation_type.value

        example_id = self.example_id

        name: None | str
        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "automationId": automation_id,
            "automationType": automation_type,
            "exampleId": example_id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automation_id = d.pop("automationId")

        automation_type = PromoteRunResponseAutomationType(d.pop("automationType"))




        example_id = d.pop("exampleId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        promote_run_response = cls(
            automation_id=automation_id,
            automation_type=automation_type,
            example_id=example_id,
            name=name,
        )

        return promote_run_response
