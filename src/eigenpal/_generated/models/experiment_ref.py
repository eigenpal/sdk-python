from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ExperimentRef")



@_attrs_define
class ExperimentRef:
    """
        Attributes:
            id (str):
            automation_id (str):
     """

    id: str
    automation_id: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        automation_id = self.automation_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "automationId": automation_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        automation_id = d.pop("automationId")

        experiment_ref = cls(
            id=id,
            automation_id=automation_id,
        )

        return experiment_ref
