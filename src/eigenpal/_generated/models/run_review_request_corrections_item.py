from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_review_request_corrections_item_kind import RunReviewRequestCorrectionsItemKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunReviewRequestCorrectionsItem")



@_attrs_define
class RunReviewRequestCorrectionsItem:
    """
        Attributes:
            kind (RunReviewRequestCorrectionsItemKind):
            path (str):
            id (str | Unset):
            label (None | str | Unset):
            original_value (Any | Unset):
            corrected_value (Any | Unset):
            note (None | str | Unset):
            corrected_artifact_path (None | str | Unset):
     """

    kind: RunReviewRequestCorrectionsItemKind
    path: str
    id: str | Unset = UNSET
    label: None | str | Unset = UNSET
    original_value: Any | Unset = UNSET
    corrected_value: Any | Unset = UNSET
    note: None | str | Unset = UNSET
    corrected_artifact_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        path = self.path

        id = self.id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        original_value = self.original_value

        corrected_value = self.corrected_value

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        corrected_artifact_path: None | str | Unset
        if isinstance(self.corrected_artifact_path, Unset):
            corrected_artifact_path = UNSET
        else:
            corrected_artifact_path = self.corrected_artifact_path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "path": path,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if original_value is not UNSET:
            field_dict["originalValue"] = original_value
        if corrected_value is not UNSET:
            field_dict["correctedValue"] = corrected_value
        if note is not UNSET:
            field_dict["note"] = note
        if corrected_artifact_path is not UNSET:
            field_dict["correctedArtifactPath"] = corrected_artifact_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = RunReviewRequestCorrectionsItemKind(d.pop("kind"))




        path = d.pop("path")

        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        original_value = d.pop("originalValue", UNSET)

        corrected_value = d.pop("correctedValue", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_corrected_artifact_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrected_artifact_path = _parse_corrected_artifact_path(d.pop("correctedArtifactPath", UNSET))


        run_review_request_corrections_item = cls(
            kind=kind,
            path=path,
            id=id,
            label=label,
            original_value=original_value,
            corrected_value=corrected_value,
            note=note,
            corrected_artifact_path=corrected_artifact_path,
        )


        run_review_request_corrections_item.additional_properties = d
        return run_review_request_corrections_item

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
