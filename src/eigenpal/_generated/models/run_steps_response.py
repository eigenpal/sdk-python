from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunStepsResponse")



@_attrs_define
class RunStepsResponse:
    """
        Attributes:
            steps (list[Any]):
     """

    steps: list[Any]





    def to_dict(self) -> dict[str, Any]:
        steps = self.steps




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "steps": steps,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        steps = cast(list[Any], d.pop("steps"))


        run_steps_response = cls(
            steps=steps,
        )

        return run_steps_response
