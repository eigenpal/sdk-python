from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_trace_event import RunTraceEvent





T = TypeVar("T", bound="RunTraceResponse")



@_attrs_define
class RunTraceResponse:
    """
        Attributes:
            events (list[RunTraceEvent]): Chronological trace events. Workflow runs return observability phases or step
                executions; agent runs return parsed trace.jsonl events.
     """

    events: list[RunTraceEvent]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_trace_event import RunTraceEvent
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "events": events,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_trace_event import RunTraceEvent
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in (_events):
            events_item = RunTraceEvent.from_dict(events_item_data)



            events.append(events_item)


        run_trace_response = cls(
            events=events,
        )

        return run_trace_response
