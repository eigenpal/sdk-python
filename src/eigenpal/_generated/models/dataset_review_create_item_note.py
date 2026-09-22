from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_item_field_note import DatasetReviewItemFieldNote





T = TypeVar("T", bound="DatasetReviewCreateItemNote")



@_attrs_define
class DatasetReviewCreateItemNote:
    """
        Attributes:
            example_name (str):
            comment (None | str | Unset):
            fields (list[DatasetReviewItemFieldNote] | Unset):
     """

    example_name: str
    comment: None | str | Unset = UNSET
    fields: list[DatasetReviewItemFieldNote] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_item_field_note import DatasetReviewItemFieldNote
        example_name = self.example_name

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "exampleName": example_name,
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_item_field_note import DatasetReviewItemFieldNote
        d = dict(src_dict)
        example_name = d.pop("exampleName")

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        _fields = d.pop("fields", UNSET)
        fields: list[DatasetReviewItemFieldNote] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = DatasetReviewItemFieldNote.from_dict(fields_item_data)



                fields.append(fields_item)


        dataset_review_create_item_note = cls(
            example_name=example_name,
            comment=comment,
            fields=fields,
        )


        dataset_review_create_item_note.additional_properties = d
        return dataset_review_create_item_note

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
