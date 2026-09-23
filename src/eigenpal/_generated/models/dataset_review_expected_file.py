from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dataset_review_expected_file_origin import DatasetReviewExpectedFileOrigin






T = TypeVar("T", bound="DatasetReviewExpectedFile")



@_attrs_define
class DatasetReviewExpectedFile:
    """
        Attributes:
            path (str): Expected-file path relative to the example expected/ folder.
            file_id (str): Version id for the current bytes. Empty for snapshot-origin files, which resolve by path.
            filename (str):
            origin (DatasetReviewExpectedFileOrigin): Whether the current bytes are the snapshotted dataset file, a
                reviewer-corrected version, or a brand-new reviewer upload.
     """

    path: str
    file_id: str
    filename: str
    origin: DatasetReviewExpectedFileOrigin





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        file_id = self.file_id

        filename = self.filename

        origin = self.origin.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
            "fileId": file_id,
            "filename": filename,
            "origin": origin,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        file_id = d.pop("fileId")

        filename = d.pop("filename")

        origin = DatasetReviewExpectedFileOrigin(d.pop("origin"))




        dataset_review_expected_file = cls(
            path=path,
            file_id=file_id,
            filename=filename,
            origin=origin,
        )

        return dataset_review_expected_file
