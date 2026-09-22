from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dataset_review_event_action import DatasetReviewEventAction
from typing import cast






T = TypeVar("T", bound="DatasetReviewEvent")



@_attrs_define
class DatasetReviewEvent:
    """
        Attributes:
            id (str):
            review_id (str):
            item_id (None | str):
            actor_user_id (None | str):
            action (DatasetReviewEventAction):
            diff_summary (Any | None):
            created_at (str):
     """

    id: str
    review_id: str
    item_id: None | str
    actor_user_id: None | str
    action: DatasetReviewEventAction
    diff_summary: Any | None
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        review_id = self.review_id

        item_id: None | str
        item_id = self.item_id

        actor_user_id: None | str
        actor_user_id = self.actor_user_id

        action = self.action.value

        diff_summary: Any | None
        diff_summary = self.diff_summary

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "reviewId": review_id,
            "itemId": item_id,
            "actorUserId": actor_user_id,
            "action": action,
            "diffSummary": diff_summary,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        review_id = d.pop("reviewId")

        def _parse_item_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item_id = _parse_item_id(d.pop("itemId"))


        def _parse_actor_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        actor_user_id = _parse_actor_user_id(d.pop("actorUserId"))


        action = DatasetReviewEventAction(d.pop("action"))




        def _parse_diff_summary(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        diff_summary = _parse_diff_summary(d.pop("diffSummary"))


        created_at = d.pop("createdAt")

        dataset_review_event = cls(
            id=id,
            review_id=review_id,
            item_id=item_id,
            actor_user_id=actor_user_id,
            action=action,
            diff_summary=diff_summary,
            created_at=created_at,
        )

        return dataset_review_event
