from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_agent_body_input import RunAgentBodyInput
  from ..models.run_agent_body_metadata import RunAgentBodyMetadata





T = TypeVar("T", bound="RunAgentBody")



@_attrs_define
class RunAgentBody:
    """ 
        Attributes:
            input_ (RunAgentBodyInput | Unset):
            field_metadata (RunAgentBodyMetadata | Unset):
     """

    input_: RunAgentBodyInput | Unset = UNSET
    field_metadata: RunAgentBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_agent_body_input import RunAgentBodyInput
        from ..models.run_agent_body_metadata import RunAgentBodyMetadata
        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_metadata, Unset):
            field_metadata = self.field_metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if field_metadata is not UNSET:
            field_dict["_metadata"] = field_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_agent_body_input import RunAgentBodyInput
        from ..models.run_agent_body_metadata import RunAgentBodyMetadata
        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: RunAgentBodyInput | Unset
        if isinstance(_input_,  Unset):
            input_ = UNSET
        else:
            input_ = RunAgentBodyInput.from_dict(_input_)




        _field_metadata = d.pop("_metadata", UNSET)
        field_metadata: RunAgentBodyMetadata | Unset
        if isinstance(_field_metadata,  Unset):
            field_metadata = UNSET
        else:
            field_metadata = RunAgentBodyMetadata.from_dict(_field_metadata)




        run_agent_body = cls(
            input_=input_,
            field_metadata=field_metadata,
        )


        run_agent_body.additional_properties = d
        return run_agent_body

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
