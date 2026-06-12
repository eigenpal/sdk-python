from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_start_body_overrides_steps import RunStartBodyOverridesSteps





T = TypeVar("T", bound="RunStartBodyOverrides")



@_attrs_define
class RunStartBodyOverrides:
    """ Per-step output overrides. Workflow runs only.

        Attributes:
            steps (RunStartBodyOverridesSteps | Unset):
     """

    steps: RunStartBodyOverridesSteps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_body_overrides_steps import RunStartBodyOverridesSteps
        steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_body_overrides_steps import RunStartBodyOverridesSteps
        d = dict(src_dict)
        _steps = d.pop("steps", UNSET)
        steps: RunStartBodyOverridesSteps | Unset
        if isinstance(_steps,  Unset):
            steps = UNSET
        else:
            steps = RunStartBodyOverridesSteps.from_dict(_steps)




        run_start_body_overrides = cls(
            steps=steps,
        )


        run_start_body_overrides.additional_properties = d
        return run_start_body_overrides

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
