from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_start_body_overrides_steps_additional_property import RunStartBodyOverridesStepsAdditionalProperty





T = TypeVar("T", bound="RunStartBodyOverridesSteps")



@_attrs_define
class RunStartBodyOverridesSteps:
    """
     """

    additional_properties: dict[str, RunStartBodyOverridesStepsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_body_overrides_steps_additional_property import RunStartBodyOverridesStepsAdditionalProperty

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_body_overrides_steps_additional_property import RunStartBodyOverridesStepsAdditionalProperty
        d = dict(src_dict)
        run_start_body_overrides_steps = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RunStartBodyOverridesStepsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        run_start_body_overrides_steps.additional_properties = additional_properties
        return run_start_body_overrides_steps

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RunStartBodyOverridesStepsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RunStartBodyOverridesStepsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
