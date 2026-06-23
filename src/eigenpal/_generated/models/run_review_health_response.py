from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_review_health_bucket import RunReviewHealthBucket
  from ..models.run_review_health_response_granularity import RunReviewHealthResponseGranularity
  from ..models.run_review_health_response_time_range import RunReviewHealthResponseTimeRange
  from ..models.run_review_health_rolling_point import RunReviewHealthRollingPoint
  from ..models.run_review_health_summary import RunReviewHealthSummary





T = TypeVar("T", bound="RunReviewHealthResponse")



@_attrs_define
class RunReviewHealthResponse:
    """
        Attributes:
            time_range (RunReviewHealthResponseTimeRange):
            granularity (RunReviewHealthResponseGranularity):
            summary (RunReviewHealthSummary):
            buckets (list[RunReviewHealthBucket]):
            rolling (list[RunReviewHealthRollingPoint]):
     """

    time_range: RunReviewHealthResponseTimeRange
    granularity: RunReviewHealthResponseGranularity
    summary: RunReviewHealthSummary
    buckets: list[RunReviewHealthBucket]
    rolling: list[RunReviewHealthRollingPoint]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_review_health_bucket import RunReviewHealthBucket
        from ..models.run_review_health_response_granularity import RunReviewHealthResponseGranularity
        from ..models.run_review_health_response_time_range import RunReviewHealthResponseTimeRange
        from ..models.run_review_health_rolling_point import RunReviewHealthRollingPoint
        from ..models.run_review_health_summary import RunReviewHealthSummary
        time_range = self.time_range.to_dict()

        granularity = self.granularity.to_dict()

        summary = self.summary.to_dict()

        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)



        rolling = []
        for rolling_item_data in self.rolling:
            rolling_item = rolling_item_data.to_dict()
            rolling.append(rolling_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "timeRange": time_range,
            "granularity": granularity,
            "summary": summary,
            "buckets": buckets,
            "rolling": rolling,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_review_health_bucket import RunReviewHealthBucket
        from ..models.run_review_health_response_granularity import RunReviewHealthResponseGranularity
        from ..models.run_review_health_response_time_range import RunReviewHealthResponseTimeRange
        from ..models.run_review_health_rolling_point import RunReviewHealthRollingPoint
        from ..models.run_review_health_summary import RunReviewHealthSummary
        d = dict(src_dict)
        time_range = RunReviewHealthResponseTimeRange.from_dict(d.pop("timeRange"))




        granularity = RunReviewHealthResponseGranularity.from_dict(d.pop("granularity"))




        summary = RunReviewHealthSummary.from_dict(d.pop("summary"))




        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in (_buckets):
            buckets_item = RunReviewHealthBucket.from_dict(buckets_item_data)



            buckets.append(buckets_item)


        rolling = []
        _rolling = d.pop("rolling")
        for rolling_item_data in (_rolling):
            rolling_item = RunReviewHealthRollingPoint.from_dict(rolling_item_data)



            rolling.append(rolling_item)


        run_review_health_response = cls(
            time_range=time_range,
            granularity=granularity,
            summary=summary,
            buckets=buckets,
            rolling=rolling,
        )

        return run_review_health_response
