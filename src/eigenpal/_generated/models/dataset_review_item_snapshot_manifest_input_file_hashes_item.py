from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DatasetReviewItemSnapshotManifestInputFileHashesItem")



@_attrs_define
class DatasetReviewItemSnapshotManifestInputFileHashesItem:
    """
        Attributes:
            path (str):
            sha256 (str):
     """

    path: str
    sha256: str





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        sha256 = self.sha256


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
            "sha256": sha256,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        sha256 = d.pop("sha256")

        dataset_review_item_snapshot_manifest_input_file_hashes_item = cls(
            path=path,
            sha256=sha256,
        )

        return dataset_review_item_snapshot_manifest_input_file_hashes_item
