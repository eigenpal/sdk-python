from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_dataset_review_request_status import UpdateDatasetReviewRequestStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_focus_field import DatasetReviewFocusField





T = TypeVar("T", bound="UpdateDatasetReviewRequest")



@_attrs_define
class UpdateDatasetReviewRequest:
    """
        Attributes:
            title (str | Unset):
            instructions (None | str | Unset):
            focus_fields (list[DatasetReviewFocusField] | Unset):
            ignored_fields (list[str] | Unset):
            status (UpdateDatasetReviewRequestStatus | Unset):
     """

    title: str | Unset = UNSET
    instructions: None | str | Unset = UNSET
    focus_fields: list[DatasetReviewFocusField] | Unset = UNSET
    ignored_fields: list[str] | Unset = UNSET
    status: UpdateDatasetReviewRequestStatus | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_focus_field import DatasetReviewFocusField
        title = self.title

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



        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if focus_fields is not UNSET:
            field_dict["focusFields"] = focus_fields
        if ignored_fields is not UNSET:
            field_dict["ignoredFields"] = ignored_fields
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_focus_field import DatasetReviewFocusField
        d = dict(src_dict)
        title = d.pop("title", UNSET)

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


        _status = d.pop("status", UNSET)
        status: UpdateDatasetReviewRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = UpdateDatasetReviewRequestStatus(_status)




        update_dataset_review_request = cls(
            title=title,
            instructions=instructions,
            focus_fields=focus_fields,
            ignored_fields=ignored_fields,
            status=status,
        )

        return update_dataset_review_request
