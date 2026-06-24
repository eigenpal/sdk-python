from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_correction_kind import RunReviewCorrectionKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunReviewCorrection")



@_attrs_define
class RunReviewCorrection:
    """
        Attributes:
            id (str):
            kind (RunReviewCorrectionKind):
            path (str): JSON Pointer for field corrections, or canonical artifact path for file reviews.
            label (None | str):
            note (str):
            created_at (str):
            updated_at (str):
            original_value (Any | None | Unset):
            corrected_value (Any | None | Unset):
            corrected_artifact_path (None | str | Unset):
     """

    id: str
    kind: RunReviewCorrectionKind
    path: str
    label: None | str
    note: str
    created_at: str
    updated_at: str
    original_value: Any | None | Unset = UNSET
    corrected_value: Any | None | Unset = UNSET
    corrected_artifact_path: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        path = self.path

        label: None | str
        label = self.label

        note = self.note

        created_at = self.created_at

        updated_at = self.updated_at

        original_value: Any | None | Unset
        if isinstance(self.original_value, Unset):
            original_value = UNSET
        else:
            original_value = self.original_value

        corrected_value: Any | None | Unset
        if isinstance(self.corrected_value, Unset):
            corrected_value = UNSET
        else:
            corrected_value = self.corrected_value

        corrected_artifact_path: None | str | Unset
        if isinstance(self.corrected_artifact_path, Unset):
            corrected_artifact_path = UNSET
        else:
            corrected_artifact_path = self.corrected_artifact_path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "path": path,
            "label": label,
            "note": note,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if original_value is not UNSET:
            field_dict["originalValue"] = original_value
        if corrected_value is not UNSET:
            field_dict["correctedValue"] = corrected_value
        if corrected_artifact_path is not UNSET:
            field_dict["correctedArtifactPath"] = corrected_artifact_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = RunReviewCorrectionKind(d.pop("kind"))




        path = d.pop("path")

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))


        note = d.pop("note")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_original_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        original_value = _parse_original_value(d.pop("originalValue", UNSET))


        def _parse_corrected_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        corrected_value = _parse_corrected_value(d.pop("correctedValue", UNSET))


        def _parse_corrected_artifact_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrected_artifact_path = _parse_corrected_artifact_path(d.pop("correctedArtifactPath", UNSET))


        run_review_correction = cls(
            id=id,
            kind=kind,
            path=path,
            label=label,
            note=note,
            created_at=created_at,
            updated_at=updated_at,
            original_value=original_value,
            corrected_value=corrected_value,
            corrected_artifact_path=corrected_artifact_path,
        )

        return run_review_correction
