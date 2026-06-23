from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunReviewExpectedFileCopyRequest")



@_attrs_define
class RunReviewExpectedFileCopyRequest:
    """ JSON request body for copying one run output file into the corrected artifact set.

        Attributes:
            output_file_name (str): Name of an existing run output file to copy into corrected artifacts.
            expected_name (str | Unset): Optional name for the copied corrected file. Defaults to the original output file
                name.
     """

    output_file_name: str
    expected_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        output_file_name = self.output_file_name

        expected_name = self.expected_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "outputFileName": output_file_name,
        })
        if expected_name is not UNSET:
            field_dict["expectedName"] = expected_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        output_file_name = d.pop("outputFileName")

        expected_name = d.pop("expectedName", UNSET)

        run_review_expected_file_copy_request = cls(
            output_file_name=output_file_name,
            expected_name=expected_name,
        )


        run_review_expected_file_copy_request.additional_properties = d
        return run_review_expected_file_copy_request

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
