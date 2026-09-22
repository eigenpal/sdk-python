from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dataset_review_field_decision_decision import DatasetReviewFieldDecisionDecision
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DatasetReviewFieldDecision")



@_attrs_define
class DatasetReviewFieldDecision:
    """
        Attributes:
            decision (DatasetReviewFieldDecisionDecision):
            reviewer_id (str):
            updated_at (str):
            comment (None | str | Unset):
     """

    decision: DatasetReviewFieldDecisionDecision
    reviewer_id: str
    updated_at: str
    comment: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        reviewer_id = self.reviewer_id

        updated_at = self.updated_at

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "decision": decision,
            "reviewerId": reviewer_id,
            "updatedAt": updated_at,
        })
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decision = DatasetReviewFieldDecisionDecision(d.pop("decision"))




        reviewer_id = d.pop("reviewerId")

        updated_at = d.pop("updatedAt")

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        dataset_review_field_decision = cls(
            decision=decision,
            reviewer_id=reviewer_id,
            updated_at=updated_at,
            comment=comment,
        )

        return dataset_review_field_decision
