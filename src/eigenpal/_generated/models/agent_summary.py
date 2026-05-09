from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_summary_config import AgentSummaryConfig
  from ..models.agent_summary_stats import AgentSummaryStats





T = TypeVar("T", bound="AgentSummary")



@_attrs_define
class AgentSummary:
    """ 
        Attributes:
            id (str):
            slug (str):
            name (str):
            created_at (str):
            description (None | str | Unset):
            config (AgentSummaryConfig | Unset):
            updated_at (str | Unset):
            stats (AgentSummaryStats | Unset):
     """

    id: str
    slug: str
    name: str
    created_at: str
    description: None | str | Unset = UNSET
    config: AgentSummaryConfig | Unset = UNSET
    updated_at: str | Unset = UNSET
    stats: AgentSummaryStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_summary_config import AgentSummaryConfig
        from ..models.agent_summary_stats import AgentSummaryStats
        id = self.id

        slug = self.slug

        name = self.name

        created_at: str
        created_at = self.created_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        updated_at: str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "slug": slug,
            "name": name,
            "createdAt": created_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_summary_config import AgentSummaryConfig
        from ..models.agent_summary_stats import AgentSummaryStats
        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        name = d.pop("name")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _config = d.pop("config", UNSET)
        config: AgentSummaryConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = AgentSummaryConfig.from_dict(_config)




        def _parse_updated_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        _stats = d.pop("stats", UNSET)
        stats: AgentSummaryStats | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = AgentSummaryStats.from_dict(_stats)




        agent_summary = cls(
            id=id,
            slug=slug,
            name=name,
            created_at=created_at,
            description=description,
            config=config,
            updated_at=updated_at,
            stats=stats,
        )


        agent_summary.additional_properties = d
        return agent_summary

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
