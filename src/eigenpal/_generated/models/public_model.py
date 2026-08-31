from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.public_model_capabilities_item import PublicModelCapabilitiesItem
from ..models.public_model_default_for_item import PublicModelDefaultForItem
from ..models.public_model_health import PublicModelHealth
from ..models.public_model_kind import PublicModelKind
from ..models.public_model_location import PublicModelLocation
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.public_model_cost import PublicModelCost
  from ..models.public_model_limits import PublicModelLimits





T = TypeVar("T", bound="PublicModel")



@_attrs_define
class PublicModel:
    """
        Attributes:
            id (str):
            kind (PublicModelKind):
            provider (str):
            label (str):
            capabilities (list[PublicModelCapabilitiesItem]):
            configured (bool):
            available (bool):
            health (PublicModelHealth): Configuration state only: `configured` means credentials are present in this
                environment; `unconfigured` means the catalog entry exists but credentials are missing. This list does not probe
                live providers, so it never reports healthy/degraded/outage. `unknown` is reserved and is not emitted by this
                endpoint.
            default_for (list[PublicModelDefaultForItem]):
            location (PublicModelLocation): `local` means on-prem / no cloud provider egress (`local: true` or tesseract).
                `hosted` means the provider is a cloud API. Endpoints are never returned.
            aliases (list[str]):
            tags (list[str]):
            limits (PublicModelLimits | Unset):
            cost (PublicModelCost | Unset):
     """

    id: str
    kind: PublicModelKind
    provider: str
    label: str
    capabilities: list[PublicModelCapabilitiesItem]
    configured: bool
    available: bool
    health: PublicModelHealth
    default_for: list[PublicModelDefaultForItem]
    location: PublicModelLocation
    aliases: list[str]
    tags: list[str]
    limits: PublicModelLimits | Unset = UNSET
    cost: PublicModelCost | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_model_cost import PublicModelCost
        from ..models.public_model_limits import PublicModelLimits
        id = self.id

        kind = self.kind.value

        provider = self.provider

        label = self.label

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.value
            capabilities.append(capabilities_item)



        configured = self.configured

        available = self.available

        health = self.health.value

        default_for = []
        for default_for_item_data in self.default_for:
            default_for_item = default_for_item_data.value
            default_for.append(default_for_item)



        location = self.location.value

        aliases = self.aliases



        tags = self.tags



        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "provider": provider,
            "label": label,
            "capabilities": capabilities,
            "configured": configured,
            "available": available,
            "health": health,
            "defaultFor": default_for,
            "location": location,
            "aliases": aliases,
            "tags": tags,
        })
        if limits is not UNSET:
            field_dict["limits"] = limits
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_model_cost import PublicModelCost
        from ..models.public_model_limits import PublicModelLimits
        d = dict(src_dict)
        id = d.pop("id")

        kind = PublicModelKind(d.pop("kind"))




        provider = d.pop("provider")

        label = d.pop("label")

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in (_capabilities):
            capabilities_item = PublicModelCapabilitiesItem(capabilities_item_data)



            capabilities.append(capabilities_item)


        configured = d.pop("configured")

        available = d.pop("available")

        health = PublicModelHealth(d.pop("health"))




        default_for = []
        _default_for = d.pop("defaultFor")
        for default_for_item_data in (_default_for):
            default_for_item = PublicModelDefaultForItem(default_for_item_data)



            default_for.append(default_for_item)


        location = PublicModelLocation(d.pop("location"))




        aliases = cast(list[str], d.pop("aliases"))


        tags = cast(list[str], d.pop("tags"))


        _limits = d.pop("limits", UNSET)
        limits: PublicModelLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = PublicModelLimits.from_dict(_limits)




        _cost = d.pop("cost", UNSET)
        cost: PublicModelCost | Unset
        if isinstance(_cost,  Unset):
            cost = UNSET
        else:
            cost = PublicModelCost.from_dict(_cost)




        public_model = cls(
            id=id,
            kind=kind,
            provider=provider,
            label=label,
            capabilities=capabilities,
            configured=configured,
            available=available,
            health=health,
            default_for=default_for,
            location=location,
            aliases=aliases,
            tags=tags,
            limits=limits,
            cost=cost,
        )

        return public_model
