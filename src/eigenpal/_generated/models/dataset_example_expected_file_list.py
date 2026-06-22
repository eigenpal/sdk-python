from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DatasetExampleExpectedFileList")



@_attrs_define
class DatasetExampleExpectedFileList:
    """
        Attributes:
            files (list[str]): Paths under the example expected folder.
     """

    files: list[str]





    def to_dict(self) -> dict[str, Any]:
        files = self.files




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "files": files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        files = cast(list[str], d.pop("files"))


        dataset_example_expected_file_list = cls(
            files=files,
        )

        return dataset_example_expected_file_list
