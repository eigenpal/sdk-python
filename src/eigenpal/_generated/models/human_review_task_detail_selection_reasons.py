from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_task_detail_selection_reasons_additional_property import HumanReviewTaskDetailSelectionReasonsAdditionalProperty






T = TypeVar("T", bound="HumanReviewTaskDetailSelectionReasons")



@_attrs_define
class HumanReviewTaskDetailSelectionReasons:
    """
     """

    additional_properties: dict[str, HumanReviewTaskDetailSelectionReasonsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        human_review_task_detail_selection_reasons = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = HumanReviewTaskDetailSelectionReasonsAdditionalProperty(prop_dict)



            additional_properties[prop_name] = additional_property

        human_review_task_detail_selection_reasons.additional_properties = additional_properties
        return human_review_task_detail_selection_reasons

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> HumanReviewTaskDetailSelectionReasonsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: HumanReviewTaskDetailSelectionReasonsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
