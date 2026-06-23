from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_health_response_granularity_bucket import RunReviewHealthResponseGranularityBucket






T = TypeVar("T", bound="RunReviewHealthResponseGranularity")



@_attrs_define
class RunReviewHealthResponseGranularity:
    """
        Attributes:
            bucket (RunReviewHealthResponseGranularityBucket):
            rolling_window (int):
            min_rolling_reviews (int):
     """

    bucket: RunReviewHealthResponseGranularityBucket
    rolling_window: int
    min_rolling_reviews: int





    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket.value

        rolling_window = self.rolling_window

        min_rolling_reviews = self.min_rolling_reviews


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "bucket": bucket,
            "rollingWindow": rolling_window,
            "minRollingReviews": min_rolling_reviews,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = RunReviewHealthResponseGranularityBucket(d.pop("bucket"))




        rolling_window = d.pop("rollingWindow")

        min_rolling_reviews = d.pop("minRollingReviews")

        run_review_health_response_granularity = cls(
            bucket=bucket,
            rolling_window=rolling_window,
            min_rolling_reviews=min_rolling_reviews,
        )

        return run_review_health_response_granularity
