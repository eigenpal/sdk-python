from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_event import DatasetReviewEvent





T = TypeVar("T", bound="DatasetReviewEventList")



@_attrs_define
class DatasetReviewEventList:
    """
        Attributes:
            events (list[DatasetReviewEvent]):
     """

    events: list[DatasetReviewEvent]





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_event import DatasetReviewEvent
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
        from ..models.dataset_review_event import DatasetReviewEvent
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in (_events):
            events_item = DatasetReviewEvent.from_dict(events_item_data)



            events.append(events_item)


        dataset_review_event_list = cls(
            events=events,
        )

        return dataset_review_event_list
