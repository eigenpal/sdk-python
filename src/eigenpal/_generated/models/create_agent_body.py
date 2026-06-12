from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_agent_body_config import CreateAgentBodyConfig





T = TypeVar("T", bound="CreateAgentBody")



@_attrs_define
class CreateAgentBody:
    """
        Attributes:
            name (str):
            slug (str):
            description (str | Unset):
            config (CreateAgentBodyConfig | Unset):
     """

    name: str
    slug: str
    description: str | Unset = UNSET
    config: CreateAgentBodyConfig | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_body_config import CreateAgentBodyConfig
        name = self.name

        slug = self.slug

        description = self.description

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "slug": slug,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_body_config import CreateAgentBodyConfig
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        description = d.pop("description", UNSET)

        _config = d.pop("config", UNSET)
        config: CreateAgentBodyConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = CreateAgentBodyConfig.from_dict(_config)




        create_agent_body = cls(
            name=name,
            slug=slug,
            description=description,
            config=config,
        )

        return create_agent_body
