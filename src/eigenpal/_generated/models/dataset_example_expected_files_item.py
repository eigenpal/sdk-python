from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DatasetExampleExpectedFilesItem")



@_attrs_define
class DatasetExampleExpectedFilesItem:
    """
        Attributes:
            name (str): Expected file name.
            url (str | Unset): Download URL for the expected file.
     """

    name: str
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url", UNSET)

        dataset_example_expected_files_item = cls(
            name=name,
            url=url,
        )

        return dataset_example_expected_files_item
