from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_files_response_outputs_by_step_additional_property_item import RunFilesResponseOutputsByStepAdditionalPropertyItem





T = TypeVar("T", bound="RunFilesResponseOutputsByStep")



@_attrs_define
class RunFilesResponseOutputsByStep:
    """
     """

    additional_properties: dict[str, list[RunFilesResponseOutputsByStepAdditionalPropertyItem]] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_files_response_outputs_by_step_additional_property_item import RunFilesResponseOutputsByStepAdditionalPropertyItem

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)




        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_files_response_outputs_by_step_additional_property_item import RunFilesResponseOutputsByStepAdditionalPropertyItem
        d = dict(src_dict)
        run_files_response_outputs_by_step = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in (_additional_property):
                additional_property_item = RunFilesResponseOutputsByStepAdditionalPropertyItem.from_dict(additional_property_item_data)



                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        run_files_response_outputs_by_step.additional_properties = additional_properties
        return run_files_response_outputs_by_step

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[RunFilesResponseOutputsByStepAdditionalPropertyItem]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[RunFilesResponseOutputsByStepAdditionalPropertyItem]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
