from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.patch_agent_body_config import PatchAgentBodyConfig





T = TypeVar("T", bound="PatchAgentBody")



@_attrs_define
class PatchAgentBody:
    """
        Attributes:
            name (str | Unset):
            description (str | Unset):
            config (PatchAgentBodyConfig | Unset):
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    config: PatchAgentBodyConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_agent_body_config import PatchAgentBodyConfig
        name = self.name

        description = self.description

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_agent_body_config import PatchAgentBodyConfig
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _config = d.pop("config", UNSET)
        config: PatchAgentBodyConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = PatchAgentBodyConfig.from_dict(_config)




        patch_agent_body = cls(
            name=name,
            description=description,
            config=config,
        )


        patch_agent_body.additional_properties = d
        return patch_agent_body

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
