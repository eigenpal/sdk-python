from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RunReviewHealthRollingPoint")



@_attrs_define
class RunReviewHealthRollingPoint:
    """
        Attributes:
            at (str):
            reviewed_runs (int): Runs with a ranked verdict (`correct` or `incorrect`). Null verdict (nit) is excluded.
            correct_reviews (int):
            reviewed_correctness (float):
            confidence_lower (float):
            confidence_upper (float):
            total_runs_in_window (int): Total production runs in the rolling window ending at this point.
            review_coverage (float): Share of runs in the rolling window that were reviewed (0-1). Uses the same window size
                as rolling accuracy, applied to all runs.
     """

    at: str
    reviewed_runs: int
    correct_reviews: int
    reviewed_correctness: float
    confidence_lower: float
    confidence_upper: float
    total_runs_in_window: int
    review_coverage: float





    def to_dict(self) -> dict[str, Any]:
        at = self.at

        reviewed_runs = self.reviewed_runs

        correct_reviews = self.correct_reviews

        reviewed_correctness = self.reviewed_correctness

        confidence_lower = self.confidence_lower

        confidence_upper = self.confidence_upper

        total_runs_in_window = self.total_runs_in_window

        review_coverage = self.review_coverage


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "at": at,
            "reviewedRuns": reviewed_runs,
            "correctReviews": correct_reviews,
            "reviewedCorrectness": reviewed_correctness,
            "confidenceLower": confidence_lower,
            "confidenceUpper": confidence_upper,
            "totalRunsInWindow": total_runs_in_window,
            "reviewCoverage": review_coverage,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = d.pop("at")

        reviewed_runs = d.pop("reviewedRuns")

        correct_reviews = d.pop("correctReviews")

        reviewed_correctness = d.pop("reviewedCorrectness")

        confidence_lower = d.pop("confidenceLower")

        confidence_upper = d.pop("confidenceUpper")

        total_runs_in_window = d.pop("totalRunsInWindow")

        review_coverage = d.pop("reviewCoverage")

        run_review_health_rolling_point = cls(
            at=at,
            reviewed_runs=reviewed_runs,
            correct_reviews=correct_reviews,
            reviewed_correctness=reviewed_correctness,
            confidence_lower=confidence_lower,
            confidence_upper=confidence_upper,
            total_runs_in_window=total_runs_in_window,
            review_coverage=review_coverage,
        )

        return run_review_health_rolling_point
