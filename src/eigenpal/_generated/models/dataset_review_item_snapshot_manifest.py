from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_item_snapshot_manifest_expected_files_item import DatasetReviewItemSnapshotManifestExpectedFilesItem
  from ..models.dataset_review_item_snapshot_manifest_input_file_hashes_item import DatasetReviewItemSnapshotManifestInputFileHashesItem
  from ..models.dataset_review_item_snapshot_manifest_metadata_type_0 import DatasetReviewItemSnapshotManifestMetadataType0





T = TypeVar("T", bound="DatasetReviewItemSnapshotManifest")



@_attrs_define
class DatasetReviewItemSnapshotManifest:
    """
        Attributes:
            expected_files (list[DatasetReviewItemSnapshotManifestExpectedFilesItem]):
            metadata (DatasetReviewItemSnapshotManifestMetadataType0 | None):
            input_file_hashes (list[DatasetReviewItemSnapshotManifestInputFileHashesItem] | Unset):
     """

    expected_files: list[DatasetReviewItemSnapshotManifestExpectedFilesItem]
    metadata: DatasetReviewItemSnapshotManifestMetadataType0 | None
    input_file_hashes: list[DatasetReviewItemSnapshotManifestInputFileHashesItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_item_snapshot_manifest_expected_files_item import DatasetReviewItemSnapshotManifestExpectedFilesItem
        from ..models.dataset_review_item_snapshot_manifest_input_file_hashes_item import DatasetReviewItemSnapshotManifestInputFileHashesItem
        from ..models.dataset_review_item_snapshot_manifest_metadata_type_0 import DatasetReviewItemSnapshotManifestMetadataType0
        expected_files = []
        for expected_files_item_data in self.expected_files:
            expected_files_item = expected_files_item_data.to_dict()
            expected_files.append(expected_files_item)



        metadata: dict[str, Any] | None
        if isinstance(self.metadata, DatasetReviewItemSnapshotManifestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        input_file_hashes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_file_hashes, Unset):
            input_file_hashes = []
            for input_file_hashes_item_data in self.input_file_hashes:
                input_file_hashes_item = input_file_hashes_item_data.to_dict()
                input_file_hashes.append(input_file_hashes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expectedFiles": expected_files,
            "metadata": metadata,
        })
        if input_file_hashes is not UNSET:
            field_dict["inputFileHashes"] = input_file_hashes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_item_snapshot_manifest_expected_files_item import DatasetReviewItemSnapshotManifestExpectedFilesItem
        from ..models.dataset_review_item_snapshot_manifest_input_file_hashes_item import DatasetReviewItemSnapshotManifestInputFileHashesItem
        from ..models.dataset_review_item_snapshot_manifest_metadata_type_0 import DatasetReviewItemSnapshotManifestMetadataType0
        d = dict(src_dict)
        expected_files = []
        _expected_files = d.pop("expectedFiles")
        for expected_files_item_data in (_expected_files):
            expected_files_item = DatasetReviewItemSnapshotManifestExpectedFilesItem.from_dict(expected_files_item_data)



            expected_files.append(expected_files_item)


        def _parse_metadata(data: object) -> DatasetReviewItemSnapshotManifestMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DatasetReviewItemSnapshotManifestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetReviewItemSnapshotManifestMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))


        _input_file_hashes = d.pop("inputFileHashes", UNSET)
        input_file_hashes: list[DatasetReviewItemSnapshotManifestInputFileHashesItem] | Unset = UNSET
        if _input_file_hashes is not UNSET:
            input_file_hashes = []
            for input_file_hashes_item_data in _input_file_hashes:
                input_file_hashes_item = DatasetReviewItemSnapshotManifestInputFileHashesItem.from_dict(input_file_hashes_item_data)



                input_file_hashes.append(input_file_hashes_item)


        dataset_review_item_snapshot_manifest = cls(
            expected_files=expected_files,
            metadata=metadata,
            input_file_hashes=input_file_hashes,
        )

        return dataset_review_item_snapshot_manifest
