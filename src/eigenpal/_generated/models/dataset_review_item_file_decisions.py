from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_file_decision import DatasetReviewFileDecision





T = TypeVar("T", bound="DatasetReviewItemFileDecisions")



@_attrs_define
class DatasetReviewItemFileDecisions:
    """ Durable per-expected-file approve/remove, keyed by expected-file path.

     """

    additional_properties: dict[str, DatasetReviewFileDecision] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_file_decision import DatasetReviewFileDecision

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_file_decision import DatasetReviewFileDecision
        d = dict(src_dict)
        dataset_review_item_file_decisions = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DatasetReviewFileDecision.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        dataset_review_item_file_decisions.additional_properties = additional_properties
        return dataset_review_item_file_decisions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DatasetReviewFileDecision:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DatasetReviewFileDecision) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
