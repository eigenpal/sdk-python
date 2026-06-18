from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ExperimentDetailRunsItem")



@_attrs_define
class ExperimentDetailRunsItem:
    """
        Attributes:
            id (str):
            status (str):
            example_id (None | str):
            example_name (None | str):
            created_at (str):
            completed_at (None | str):
     """

    id: str
    status: str
    example_id: None | str
    example_name: None | str
    created_at: str
    completed_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        example_id: None | str
        example_id = self.example_id

        example_name: None | str
        example_name = self.example_name

        created_at: str
        created_at = self.created_at

        completed_at: None | str
        completed_at = self.completed_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "status": status,
            "exampleId": example_id,
            "exampleName": example_name,
            "createdAt": created_at,
            "completedAt": completed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        def _parse_example_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        example_id = _parse_example_id(d.pop("exampleId"))


        def _parse_example_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        example_name = _parse_example_name(d.pop("exampleName"))


        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))


        experiment_detail_runs_item = cls(
            id=id,
            status=status,
            example_id=example_id,
            example_name=example_name,
            created_at=created_at,
            completed_at=completed_at,
        )

        return experiment_detail_runs_item
