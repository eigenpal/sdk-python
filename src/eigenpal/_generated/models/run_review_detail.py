from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_review import RunReview





T = TypeVar("T", bound="RunReviewDetail")



@_attrs_define
class RunReviewDetail:
    """
        Attributes:
            review (None | RunReview): Review metadata and corrections. Corrected files are listed separately at GET
                /runs/{id}/reviews/expected.
     """

    review: None | RunReview





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_review import RunReview
        review: dict[str, Any] | None
        if isinstance(self.review, RunReview):
            review = self.review.to_dict()
        else:
            review = self.review


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "review": review,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_review import RunReview
        d = dict(src_dict)
        def _parse_review(data: object) -> None | RunReview:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                review_type_0 = RunReview.from_dict(data)



                return review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunReview, data)

        review = _parse_review(d.pop("review"))


        run_review_detail = cls(
            review=review,
        )

        return run_review_detail
