from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_versions_response_versions_item import ListAgentVersionsResponseVersionsItem





T = TypeVar("T", bound="ListAgentVersionsResponse")



@_attrs_define
class ListAgentVersionsResponse:
    """ 
        Attributes:
            agent_id (str):
            slug (str):
            package_path (str):
            versions (list[ListAgentVersionsResponseVersionsItem]):
     """

    agent_id: str
    slug: str
    package_path: str
    versions: list[ListAgentVersionsResponseVersionsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_versions_response_versions_item import ListAgentVersionsResponseVersionsItem
        agent_id = self.agent_id

        slug = self.slug

        package_path = self.package_path

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agentId": agent_id,
            "slug": slug,
            "packagePath": package_path,
            "versions": versions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_versions_response_versions_item import ListAgentVersionsResponseVersionsItem
        d = dict(src_dict)
        agent_id = d.pop("agentId")

        slug = d.pop("slug")

        package_path = d.pop("packagePath")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in (_versions):
            versions_item = ListAgentVersionsResponseVersionsItem.from_dict(versions_item_data)



            versions.append(versions_item)


        list_agent_versions_response = cls(
            agent_id=agent_id,
            slug=slug,
            package_path=package_path,
            versions=versions,
        )

        return list_agent_versions_response

