from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.example_run_response_type import ExampleRunResponseType
from typing import cast






T = TypeVar("T", bound="ExampleRunResponse")



@_attrs_define
class ExampleRunResponse:
    """
        Attributes:
            id (str):
            type_ (ExampleRunResponseType):
            batch_id (None | str):
            finished (bool):
     """

    id: str
    type_: ExampleRunResponseType
    batch_id: None | str
    finished: bool





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        batch_id: None | str
        batch_id = self.batch_id

        finished = self.finished


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "batchId": batch_id,
            "finished": finished,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = ExampleRunResponseType(d.pop("type"))




        def _parse_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        batch_id = _parse_batch_id(d.pop("batchId"))


        finished = d.pop("finished")

        example_run_response = cls(
            id=id,
            type_=type_,
            batch_id=batch_id,
            finished=finished,
        )

        return example_run_response
