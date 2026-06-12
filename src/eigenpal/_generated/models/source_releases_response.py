from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.source_releases_response_releases_item import SourceReleasesResponseReleasesItem





T = TypeVar("T", bound="SourceReleasesResponse")



@_attrs_define
class SourceReleasesResponse:
    """
        Attributes:
            package_path (str):
            releases (list[SourceReleasesResponseReleasesItem]):
     """

    package_path: str
    releases: list[SourceReleasesResponseReleasesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_releases_response_releases_item import SourceReleasesResponseReleasesItem
        package_path = self.package_path

        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "packagePath": package_path,
            "releases": releases,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_releases_response_releases_item import SourceReleasesResponseReleasesItem
        d = dict(src_dict)
        package_path = d.pop("packagePath")

        releases = []
        _releases = d.pop("releases")
        for releases_item_data in (_releases):
            releases_item = SourceReleasesResponseReleasesItem.from_dict(releases_item_data)



            releases.append(releases_item)


        source_releases_response = cls(
            package_path=package_path,
            releases=releases,
        )

        return source_releases_response
