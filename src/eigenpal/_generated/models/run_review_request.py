from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_request_status import RunReviewRequestStatus
from ..models.run_review_request_verdict_type_0 import RunReviewRequestVerdictType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_review_request_corrections_item import RunReviewRequestCorrectionsItem





T = TypeVar("T", bound="RunReviewRequest")



@_attrs_define
class RunReviewRequest:
    """ Create or replace review metadata for a run. Attribution fields (`reviewedBy`, `closedBy`, and their emails) are
    read-only and populated from the authenticated user or API key creator.

        Attributes:
            verdict (None | RunReviewRequestVerdictType0 | Unset): Reviewer verdict. Omit or send null for feedback without
                a ranking (nit). Defaults are applied client-side only; any verdict/status combination is accepted.
            status (RunReviewRequestStatus | Unset): Review lifecycle. Defaults from verdict (`correct` → `closed`,
                otherwise `open`). Use `closed` or `wont_fix` to close an open review.
            note (None | str | Unset): Reviewer note.
            corrected_output (Any | None | Unset): Corrected JSON output for this run. Send `null` to clear a previously
                stored correction.
            corrections (list[RunReviewRequestCorrectionsItem] | Unset): Field and file corrections. When present, replaces
                the entire correction set for this review. Omit to leave existing corrections unchanged.
     """

    verdict: None | RunReviewRequestVerdictType0 | Unset = UNSET
    status: RunReviewRequestStatus | Unset = UNSET
    note: None | str | Unset = UNSET
    corrected_output: Any | None | Unset = UNSET
    corrections: list[RunReviewRequestCorrectionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_review_request_corrections_item import RunReviewRequestCorrectionsItem
        verdict: None | str | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(self.verdict, RunReviewRequestVerdictType0):
            verdict = self.verdict.value
        else:
            verdict = self.verdict

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        corrected_output: Any | None | Unset
        if isinstance(self.corrected_output, Unset):
            corrected_output = UNSET
        else:
            corrected_output = self.corrected_output

        corrections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.corrections, Unset):
            corrections = []
            for corrections_item_data in self.corrections:
                corrections_item = corrections_item_data.to_dict()
                corrections.append(corrections_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if status is not UNSET:
            field_dict["status"] = status
        if note is not UNSET:
            field_dict["note"] = note
        if corrected_output is not UNSET:
            field_dict["correctedOutput"] = corrected_output
        if corrections is not UNSET:
            field_dict["corrections"] = corrections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_review_request_corrections_item import RunReviewRequestCorrectionsItem
        d = dict(src_dict)
        def _parse_verdict(data: object) -> None | RunReviewRequestVerdictType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_0 = RunReviewRequestVerdictType0(data)



                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunReviewRequestVerdictType0 | Unset, data)

        verdict = _parse_verdict(d.pop("verdict", UNSET))


        _status = d.pop("status", UNSET)
        status: RunReviewRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RunReviewRequestStatus(_status)




        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_corrected_output(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        corrected_output = _parse_corrected_output(d.pop("correctedOutput", UNSET))


        _corrections = d.pop("corrections", UNSET)
        corrections: list[RunReviewRequestCorrectionsItem] | Unset = UNSET
        if _corrections is not UNSET:
            corrections = []
            for corrections_item_data in _corrections:
                corrections_item = RunReviewRequestCorrectionsItem.from_dict(corrections_item_data)



                corrections.append(corrections_item)


        run_review_request = cls(
            verdict=verdict,
            status=status,
            note=note,
            corrected_output=corrected_output,
            corrections=corrections,
        )


        run_review_request.additional_properties = d
        return run_review_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
