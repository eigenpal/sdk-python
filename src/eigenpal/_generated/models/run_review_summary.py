from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_summary_status import RunReviewSummaryStatus
from ..models.run_review_summary_verdict_type_0 import RunReviewSummaryVerdictType0
from typing import cast






T = TypeVar("T", bound="RunReviewSummary")



@_attrs_define
class RunReviewSummary:
    """
        Attributes:
            verdict (None | RunReviewSummaryVerdictType0):
            status (RunReviewSummaryStatus):
            has_note (bool): True when review notes were left.
            correction_count (int): Number of field/file corrections.
     """

    verdict: None | RunReviewSummaryVerdictType0
    status: RunReviewSummaryStatus
    has_note: bool
    correction_count: int





    def to_dict(self) -> dict[str, Any]:
        verdict: None | str
        if isinstance(self.verdict, RunReviewSummaryVerdictType0):
            verdict = self.verdict.value
        else:
            verdict = self.verdict

        status = self.status.value

        has_note = self.has_note

        correction_count = self.correction_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "verdict": verdict,
            "status": status,
            "hasNote": has_note,
            "correctionCount": correction_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_verdict(data: object) -> None | RunReviewSummaryVerdictType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_0 = RunReviewSummaryVerdictType0(data)



                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunReviewSummaryVerdictType0, data)

        verdict = _parse_verdict(d.pop("verdict"))


        status = RunReviewSummaryStatus(d.pop("status"))




        has_note = d.pop("hasNote")

        correction_count = d.pop("correctionCount")

        run_review_summary = cls(
            verdict=verdict,
            status=status,
            has_note=has_note,
            correction_count=correction_count,
        )

        return run_review_summary
