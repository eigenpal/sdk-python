from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_workflow_body_trigger import RunWorkflowBodyTrigger
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_workflow_body_input import RunWorkflowBodyInput
  from ..models.run_workflow_body_overrides_type_0 import RunWorkflowBodyOverridesType0





T = TypeVar("T", bound="RunWorkflowBody")



@_attrs_define
class RunWorkflowBody:
    """ 
        Attributes:
            input_ (RunWorkflowBodyInput | Unset): Workflow inputs keyed by input name
            overrides (None | RunWorkflowBodyOverridesType0 | Unset): Per-step output overrides for replay
            trigger (RunWorkflowBodyTrigger | Unset): Caller surface (defaults to "api")
     """

    input_: RunWorkflowBodyInput | Unset = UNSET
    overrides: None | RunWorkflowBodyOverridesType0 | Unset = UNSET
    trigger: RunWorkflowBodyTrigger | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_workflow_body_input import RunWorkflowBodyInput
        from ..models.run_workflow_body_overrides_type_0 import RunWorkflowBodyOverridesType0
        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        overrides: dict[str, Any] | None | Unset
        if isinstance(self.overrides, Unset):
            overrides = UNSET
        elif isinstance(self.overrides, RunWorkflowBodyOverridesType0):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_workflow_body_input import RunWorkflowBodyInput
        from ..models.run_workflow_body_overrides_type_0 import RunWorkflowBodyOverridesType0
        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: RunWorkflowBodyInput | Unset
        if isinstance(_input_,  Unset):
            input_ = UNSET
        else:
            input_ = RunWorkflowBodyInput.from_dict(_input_)




        def _parse_overrides(data: object) -> None | RunWorkflowBodyOverridesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = RunWorkflowBodyOverridesType0.from_dict(data)



                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunWorkflowBodyOverridesType0 | Unset, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))


        _trigger = d.pop("trigger", UNSET)
        trigger: RunWorkflowBodyTrigger | Unset
        if isinstance(_trigger,  Unset):
            trigger = UNSET
        else:
            trigger = RunWorkflowBodyTrigger(_trigger)




        run_workflow_body = cls(
            input_=input_,
            overrides=overrides,
            trigger=trigger,
        )

        return run_workflow_body

