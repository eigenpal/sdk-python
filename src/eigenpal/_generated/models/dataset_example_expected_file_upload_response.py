from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DatasetExampleExpectedFileUploadResponse")



@_attrs_define
class DatasetExampleExpectedFileUploadResponse:
    """
        Attributes:
            uploaded (list[str]): Stored expected file paths.
     """

    uploaded: list[str]





    def to_dict(self) -> dict[str, Any]:
        uploaded = self.uploaded




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "uploaded": uploaded,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uploaded = cast(list[str], d.pop("uploaded"))


        dataset_example_expected_file_upload_response = cls(
            uploaded=uploaded,
        )

        return dataset_example_expected_file_upload_response
