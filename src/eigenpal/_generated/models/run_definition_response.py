from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RunDefinitionResponse")



@_attrs_define
class RunDefinitionResponse:
    """
        Attributes:
            definition (Any): The workflow definition snapshot captured when the run was created.
     """

    definition: Any





    def to_dict(self) -> dict[str, Any]:
        definition = self.definition


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "definition": definition,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        definition = d.pop("definition")

        run_definition_response = cls(
            definition=definition,
        )

        return run_definition_response
