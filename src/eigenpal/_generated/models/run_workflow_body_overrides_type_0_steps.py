from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_workflow_body_overrides_type_0_steps_additional_property import RunWorkflowBodyOverridesType0StepsAdditionalProperty





T = TypeVar("T", bound="RunWorkflowBodyOverridesType0Steps")



@_attrs_define
class RunWorkflowBodyOverridesType0Steps:
    """ 
     """

    additional_properties: dict[str, RunWorkflowBodyOverridesType0StepsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_workflow_body_overrides_type_0_steps_additional_property import RunWorkflowBodyOverridesType0StepsAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_workflow_body_overrides_type_0_steps_additional_property import RunWorkflowBodyOverridesType0StepsAdditionalProperty
        d = dict(src_dict)
        run_workflow_body_overrides_type_0_steps = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RunWorkflowBodyOverridesType0StepsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        run_workflow_body_overrides_type_0_steps.additional_properties = additional_properties
        return run_workflow_body_overrides_type_0_steps

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RunWorkflowBodyOverridesType0StepsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RunWorkflowBodyOverridesType0StepsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
