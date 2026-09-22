from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_dataset_review_request_status import CreateDatasetReviewRequestStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_create_item_note import DatasetReviewCreateItemNote
  from ..models.dataset_review_focus_field import DatasetReviewFocusField





T = TypeVar("T", bound="CreateDatasetReviewRequest")



@_attrs_define
class CreateDatasetReviewRequest:
    """
        Attributes:
            title (str):
            example_names (list[str]):
            instructions (None | str | Unset): Note shown to the reviewer for the whole request.
            focus_fields (list[DatasetReviewFocusField] | Unset): Expected-output paths to highlight. Other fields stay
                normal unless listed in ignoredFields.
            ignored_fields (list[str] | Unset): Expected-output paths reviewers can skip. Shown muted as not required.
                Prefixes apply to nested leaves.
            item_notes (list[DatasetReviewCreateItemNote] | Unset): Optional per-example and per-field notes seeded as
                commented events at create time.
            status (CreateDatasetReviewRequestStatus | Unset):
     """

    title: str
    example_names: list[str]
    instructions: None | str | Unset = UNSET
    focus_fields: list[DatasetReviewFocusField] | Unset = UNSET
    ignored_fields: list[str] | Unset = UNSET
    item_notes: list[DatasetReviewCreateItemNote] | Unset = UNSET
    status: CreateDatasetReviewRequestStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_create_item_note import DatasetReviewCreateItemNote
        from ..models.dataset_review_focus_field import DatasetReviewFocusField
        title = self.title

        example_names = self.example_names



        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        focus_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.focus_fields, Unset):
            focus_fields = []
            for focus_fields_item_data in self.focus_fields:
                focus_fields_item = focus_fields_item_data.to_dict()
                focus_fields.append(focus_fields_item)



        ignored_fields: list[str] | Unset = UNSET
        if not isinstance(self.ignored_fields, Unset):
            ignored_fields = self.ignored_fields



        item_notes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_notes, Unset):
            item_notes = []
            for item_notes_item_data in self.item_notes:
                item_notes_item = item_notes_item_data.to_dict()
                item_notes.append(item_notes_item)



        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "title": title,
            "exampleNames": example_names,
        })
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if focus_fields is not UNSET:
            field_dict["focusFields"] = focus_fields
        if ignored_fields is not UNSET:
            field_dict["ignoredFields"] = ignored_fields
        if item_notes is not UNSET:
            field_dict["itemNotes"] = item_notes
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_create_item_note import DatasetReviewCreateItemNote
        from ..models.dataset_review_focus_field import DatasetReviewFocusField
        d = dict(src_dict)
        title = d.pop("title")

        example_names = cast(list[str], d.pop("exampleNames"))


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        _focus_fields = d.pop("focusFields", UNSET)
        focus_fields: list[DatasetReviewFocusField] | Unset = UNSET
        if _focus_fields is not UNSET:
            focus_fields = []
            for focus_fields_item_data in _focus_fields:
                focus_fields_item = DatasetReviewFocusField.from_dict(focus_fields_item_data)



                focus_fields.append(focus_fields_item)


        ignored_fields = cast(list[str], d.pop("ignoredFields", UNSET))


        _item_notes = d.pop("itemNotes", UNSET)
        item_notes: list[DatasetReviewCreateItemNote] | Unset = UNSET
        if _item_notes is not UNSET:
            item_notes = []
            for item_notes_item_data in _item_notes:
                item_notes_item = DatasetReviewCreateItemNote.from_dict(item_notes_item_data)



                item_notes.append(item_notes_item)


        _status = d.pop("status", UNSET)
        status: CreateDatasetReviewRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = CreateDatasetReviewRequestStatus(_status)




        create_dataset_review_request = cls(
            title=title,
            example_names=example_names,
            instructions=instructions,
            focus_fields=focus_fields,
            ignored_fields=ignored_fields,
            item_notes=item_notes,
            status=status,
        )


        create_dataset_review_request.additional_properties = d
        return create_dataset_review_request

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
