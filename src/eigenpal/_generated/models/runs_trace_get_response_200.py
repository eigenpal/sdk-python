from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunsTraceGetResponse200")



@_attrs_define
class RunsTraceGetResponse200:
    """ 
        Attributes:
            events (list[Any]):
     """

    events: list[Any]





    def to_dict(self) -> dict[str, Any]:
        events = self.events




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "events": events,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = cast(list[Any], d.pop("events"))


        runs_trace_get_response_200 = cls(
            events=events,
        )

        return runs_trace_get_response_200

