from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_status import RunReviewStatus
from ..models.run_review_verdict_type_0 import RunReviewVerdictType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_review_correction import RunReviewCorrection





T = TypeVar("T", bound="RunReview")



@_attrs_define
class RunReview:
    """
        Attributes:
            id (str):
            verdict (None | RunReviewVerdictType0):
            status (RunReviewStatus):
            note (str):
            reviewed_by (None | str): User id of the last reviewer. Read-only; set from the authenticated user or API key
                creator.
            reviewed_by_email (None | str): Email of the last reviewer. Read-only; set from the authenticated user or API
                key creator.
            reviewed_at (str):
            closed_by (None | str): User id recorded when the review was closed. Read-only; set when status becomes closed
                or wont_fix.
            closed_by_email (None | str): Email recorded when the review was closed. Read-only; set when status becomes
                closed or wont_fix.
            closed_at (None | str):
            closed_note (None | str):
            created_at (str):
            updated_at (str):
            corrections (list[RunReviewCorrection]):
            corrected_output (Any | None | Unset):
     """

    id: str
    verdict: None | RunReviewVerdictType0
    status: RunReviewStatus
    note: str
    reviewed_by: None | str
    reviewed_by_email: None | str
    reviewed_at: str
    closed_by: None | str
    closed_by_email: None | str
    closed_at: None | str
    closed_note: None | str
    created_at: str
    updated_at: str
    corrections: list[RunReviewCorrection]
    corrected_output: Any | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_review_correction import RunReviewCorrection
        id = self.id

        verdict: None | str
        if isinstance(self.verdict, RunReviewVerdictType0):
            verdict = self.verdict.value
        else:
            verdict = self.verdict

        status = self.status.value

        note = self.note

        reviewed_by: None | str
        reviewed_by = self.reviewed_by

        reviewed_by_email: None | str
        reviewed_by_email = self.reviewed_by_email

        reviewed_at = self.reviewed_at

        closed_by: None | str
        closed_by = self.closed_by

        closed_by_email: None | str
        closed_by_email = self.closed_by_email

        closed_at: None | str
        closed_at = self.closed_at

        closed_note: None | str
        closed_note = self.closed_note

        created_at = self.created_at

        updated_at = self.updated_at

        corrections = []
        for corrections_item_data in self.corrections:
            corrections_item = corrections_item_data.to_dict()
            corrections.append(corrections_item)



        corrected_output: Any | None | Unset
        if isinstance(self.corrected_output, Unset):
            corrected_output = UNSET
        else:
            corrected_output = self.corrected_output


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "verdict": verdict,
            "status": status,
            "note": note,
            "reviewedBy": reviewed_by,
            "reviewedByEmail": reviewed_by_email,
            "reviewedAt": reviewed_at,
            "closedBy": closed_by,
            "closedByEmail": closed_by_email,
            "closedAt": closed_at,
            "closedNote": closed_note,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "corrections": corrections,
        })
        if corrected_output is not UNSET:
            field_dict["correctedOutput"] = corrected_output

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_review_correction import RunReviewCorrection
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_verdict(data: object) -> None | RunReviewVerdictType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_0 = RunReviewVerdictType0(data)



                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunReviewVerdictType0, data)

        verdict = _parse_verdict(d.pop("verdict"))


        status = RunReviewStatus(d.pop("status"))




        note = d.pop("note")

        def _parse_reviewed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewed_by = _parse_reviewed_by(d.pop("reviewedBy"))


        def _parse_reviewed_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewed_by_email = _parse_reviewed_by_email(d.pop("reviewedByEmail"))


        reviewed_at = d.pop("reviewedAt")

        def _parse_closed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_by = _parse_closed_by(d.pop("closedBy"))


        def _parse_closed_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_by_email = _parse_closed_by_email(d.pop("closedByEmail"))


        def _parse_closed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_at = _parse_closed_at(d.pop("closedAt"))


        def _parse_closed_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_note = _parse_closed_note(d.pop("closedNote"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        corrections = []
        _corrections = d.pop("corrections")
        for corrections_item_data in (_corrections):
            corrections_item = RunReviewCorrection.from_dict(corrections_item_data)



            corrections.append(corrections_item)


        def _parse_corrected_output(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        corrected_output = _parse_corrected_output(d.pop("correctedOutput", UNSET))


        run_review = cls(
            id=id,
            verdict=verdict,
            status=status,
            note=note,
            reviewed_by=reviewed_by,
            reviewed_by_email=reviewed_by_email,
            reviewed_at=reviewed_at,
            closed_by=closed_by,
            closed_by_email=closed_by_email,
            closed_at=closed_at,
            closed_note=closed_note,
            created_at=created_at,
            updated_at=updated_at,
            corrections=corrections,
            corrected_output=corrected_output,
        )

        return run_review
