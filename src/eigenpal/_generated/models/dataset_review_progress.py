from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DatasetReviewProgress")



@_attrs_define
class DatasetReviewProgress:
    """
        Attributes:
            total (int):
            pending (int):
            approved (int):
            edited (int):
            rejected (int):
            remaining (int): Count of examples still pending a decision.
            complete (bool): True when every example has been approved, edited, or rejected. Close the request when review
                is finished; dataset write-back is always manual.
     """

    total: int
    pending: int
    approved: int
    edited: int
    rejected: int
    remaining: int
    complete: bool





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        approved = self.approved

        edited = self.edited

        rejected = self.rejected

        remaining = self.remaining

        complete = self.complete


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "total": total,
            "pending": pending,
            "approved": approved,
            "edited": edited,
            "rejected": rejected,
            "remaining": remaining,
            "complete": complete,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        pending = d.pop("pending")

        approved = d.pop("approved")

        edited = d.pop("edited")

        rejected = d.pop("rejected")

        remaining = d.pop("remaining")

        complete = d.pop("complete")

        dataset_review_progress = cls(
            total=total,
            pending=pending,
            approved=approved,
            edited=edited,
            rejected=rejected,
            remaining=remaining,
            complete=complete,
        )

        return dataset_review_progress
