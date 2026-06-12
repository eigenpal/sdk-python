from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Schema0")



@_attrs_define
class Schema0:
    """
        Attributes:
            package_path (str):
            requested_ref (str):
            resolved_ref (str):
            commit (str):
            dependencies (list[Schema0]):
            resolved_tag (str | Unset):
     """

    package_path: str
    requested_ref: str
    resolved_ref: str
    commit: str
    dependencies: list[Schema0]
    resolved_tag: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        package_path = self.package_path

        requested_ref = self.requested_ref

        resolved_ref = self.resolved_ref

        commit = self.commit

        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)



        resolved_tag = self.resolved_tag


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "packagePath": package_path,
            "requestedRef": requested_ref,
            "resolvedRef": resolved_ref,
            "commit": commit,
            "dependencies": dependencies,
        })
        if resolved_tag is not UNSET:
            field_dict["resolvedTag"] = resolved_tag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_path = d.pop("packagePath")

        requested_ref = d.pop("requestedRef")

        resolved_ref = d.pop("resolvedRef")

        commit = d.pop("commit")

        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in (_dependencies):
            dependencies_item = Schema0.from_dict(dependencies_item_data)



            dependencies.append(dependencies_item)


        resolved_tag = d.pop("resolvedTag", UNSET)

        schema_0 = cls(
            package_path=package_path,
            requested_ref=requested_ref,
            resolved_ref=resolved_ref,
            commit=commit,
            dependencies=dependencies,
            resolved_tag=resolved_tag,
        )

        return schema_0
