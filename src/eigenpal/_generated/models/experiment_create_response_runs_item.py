from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ExperimentCreateResponseRunsItem")



@_attrs_define
class ExperimentCreateResponseRunsItem:
    """
        Attributes:
            id (str): Run id.
            example_id (None | str): Dataset example id.
     """

    id: str
    example_id: None | str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        example_id: None | str
        example_id = self.example_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "exampleId": example_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_example_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        example_id = _parse_example_id(d.pop("exampleId"))


        experiment_create_response_runs_item = cls(
            id=id,
            example_id=example_id,
        )

        return experiment_create_response_runs_item
