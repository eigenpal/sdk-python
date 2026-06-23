from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_review_health_confidence import RunReviewHealthConfidence





T = TypeVar("T", bound="RunReviewHealthSummary")



@_attrs_define
class RunReviewHealthSummary:
    """
        Attributes:
            total_runs (int):
            reviewed_runs (int): Runs with a ranked verdict (`correct` or `incorrect`). Null verdict (nit) is excluded.
            review_coverage (float | None):
            correct_reviews (int):
            incorrect_reviews (int):
            nit_reviews (int): Runs with a review row and null verdict (nit). Excluded from review coverage and accuracy.
            reviewed_correctness (float | None):
            confidence (RunReviewHealthConfidence): Wilson score confidence interval for reviewed correctness. Null bounds
                mean there are no reviewed runs in the sample.
     """

    total_runs: int
    reviewed_runs: int
    review_coverage: float | None
    correct_reviews: int
    incorrect_reviews: int
    nit_reviews: int
    reviewed_correctness: float | None
    confidence: RunReviewHealthConfidence





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_review_health_confidence import RunReviewHealthConfidence
        total_runs = self.total_runs

        reviewed_runs = self.reviewed_runs

        review_coverage: float | None
        review_coverage = self.review_coverage

        correct_reviews = self.correct_reviews

        incorrect_reviews = self.incorrect_reviews

        nit_reviews = self.nit_reviews

        reviewed_correctness: float | None
        reviewed_correctness = self.reviewed_correctness

        confidence = self.confidence.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "totalRuns": total_runs,
            "reviewedRuns": reviewed_runs,
            "reviewCoverage": review_coverage,
            "correctReviews": correct_reviews,
            "incorrectReviews": incorrect_reviews,
            "nitReviews": nit_reviews,
            "reviewedCorrectness": reviewed_correctness,
            "confidence": confidence,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_review_health_confidence import RunReviewHealthConfidence
        d = dict(src_dict)
        total_runs = d.pop("totalRuns")

        reviewed_runs = d.pop("reviewedRuns")

        def _parse_review_coverage(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        review_coverage = _parse_review_coverage(d.pop("reviewCoverage"))


        correct_reviews = d.pop("correctReviews")

        incorrect_reviews = d.pop("incorrectReviews")

        nit_reviews = d.pop("nitReviews")

        def _parse_reviewed_correctness(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        reviewed_correctness = _parse_reviewed_correctness(d.pop("reviewedCorrectness"))


        confidence = RunReviewHealthConfidence.from_dict(d.pop("confidence"))




        run_review_health_summary = cls(
            total_runs=total_runs,
            reviewed_runs=reviewed_runs,
            review_coverage=review_coverage,
            correct_reviews=correct_reviews,
            incorrect_reviews=incorrect_reviews,
            nit_reviews=nit_reviews,
            reviewed_correctness=reviewed_correctness,
            confidence=confidence,
        )

        return run_review_health_summary
