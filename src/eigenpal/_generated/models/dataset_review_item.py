from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dataset_review_item_status import DatasetReviewItemStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_expected_file import DatasetReviewExpectedFile
  from ..models.dataset_review_item_field_decisions import DatasetReviewItemFieldDecisions
  from ..models.dataset_review_item_file_decisions import DatasetReviewItemFileDecisions
  from ..models.dataset_review_item_snapshot_input_json_type_0 import DatasetReviewItemSnapshotInputJsonType0
  from ..models.dataset_review_item_snapshot_manifest import DatasetReviewItemSnapshotManifest





T = TypeVar("T", bound="DatasetReviewItem")



@_attrs_define
class DatasetReviewItem:
    """
        Attributes:
            id (str):
            review_id (str):
            example_name (str):
            snapshot_input_json (DatasetReviewItemSnapshotInputJsonType0 | None):
            snapshot_expected_json (Any | None):
            snapshot_manifest (DatasetReviewItemSnapshotManifest):
            status (DatasetReviewItemStatus):
            current_expected_json (Any | None):
            field_decisions (DatasetReviewItemFieldDecisions):
            current_expected_files (list[DatasetReviewExpectedFile] | None): Overlay of the snapshot manifest expected
                files. Null means pristine — the reviewer has not corrected or uploaded any file yet.
            file_decisions (DatasetReviewItemFileDecisions): Durable per-expected-file approve/reject, keyed by expected-
                file path.
            input_drifted (bool): True when live dataset input-file bytes no longer match the hashes captured at request
                creation.
            updated_by (None | str):
            updated_at (str):
     """

    id: str
    review_id: str
    example_name: str
    snapshot_input_json: DatasetReviewItemSnapshotInputJsonType0 | None
    snapshot_expected_json: Any | None
    snapshot_manifest: DatasetReviewItemSnapshotManifest
    status: DatasetReviewItemStatus
    current_expected_json: Any | None
    field_decisions: DatasetReviewItemFieldDecisions
    current_expected_files: list[DatasetReviewExpectedFile] | None
    file_decisions: DatasetReviewItemFileDecisions
    input_drifted: bool
    updated_by: None | str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_expected_file import DatasetReviewExpectedFile
        from ..models.dataset_review_item_field_decisions import DatasetReviewItemFieldDecisions
        from ..models.dataset_review_item_file_decisions import DatasetReviewItemFileDecisions
        from ..models.dataset_review_item_snapshot_input_json_type_0 import DatasetReviewItemSnapshotInputJsonType0
        from ..models.dataset_review_item_snapshot_manifest import DatasetReviewItemSnapshotManifest
        id = self.id

        review_id = self.review_id

        example_name = self.example_name

        snapshot_input_json: dict[str, Any] | None
        if isinstance(self.snapshot_input_json, DatasetReviewItemSnapshotInputJsonType0):
            snapshot_input_json = self.snapshot_input_json.to_dict()
        else:
            snapshot_input_json = self.snapshot_input_json

        snapshot_expected_json: Any | None
        snapshot_expected_json = self.snapshot_expected_json

        snapshot_manifest = self.snapshot_manifest.to_dict()

        status = self.status.value

        current_expected_json: Any | None
        current_expected_json = self.current_expected_json

        field_decisions = self.field_decisions.to_dict()

        current_expected_files: list[dict[str, Any]] | None
        if isinstance(self.current_expected_files, list):
            current_expected_files = []
            for current_expected_files_type_0_item_data in self.current_expected_files:
                current_expected_files_type_0_item = current_expected_files_type_0_item_data.to_dict()
                current_expected_files.append(current_expected_files_type_0_item)


        else:
            current_expected_files = self.current_expected_files

        file_decisions = self.file_decisions.to_dict()

        input_drifted = self.input_drifted

        updated_by: None | str
        updated_by = self.updated_by

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "reviewId": review_id,
            "exampleName": example_name,
            "snapshotInputJson": snapshot_input_json,
            "snapshotExpectedJson": snapshot_expected_json,
            "snapshotManifest": snapshot_manifest,
            "status": status,
            "currentExpectedJson": current_expected_json,
            "fieldDecisions": field_decisions,
            "currentExpectedFiles": current_expected_files,
            "fileDecisions": file_decisions,
            "inputDrifted": input_drifted,
            "updatedBy": updated_by,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_expected_file import DatasetReviewExpectedFile
        from ..models.dataset_review_item_field_decisions import DatasetReviewItemFieldDecisions
        from ..models.dataset_review_item_file_decisions import DatasetReviewItemFileDecisions
        from ..models.dataset_review_item_snapshot_input_json_type_0 import DatasetReviewItemSnapshotInputJsonType0
        from ..models.dataset_review_item_snapshot_manifest import DatasetReviewItemSnapshotManifest
        d = dict(src_dict)
        id = d.pop("id")

        review_id = d.pop("reviewId")

        example_name = d.pop("exampleName")

        def _parse_snapshot_input_json(data: object) -> DatasetReviewItemSnapshotInputJsonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                snapshot_input_json_type_0 = DatasetReviewItemSnapshotInputJsonType0.from_dict(data)



                return snapshot_input_json_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetReviewItemSnapshotInputJsonType0 | None, data)

        snapshot_input_json = _parse_snapshot_input_json(d.pop("snapshotInputJson"))


        def _parse_snapshot_expected_json(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        snapshot_expected_json = _parse_snapshot_expected_json(d.pop("snapshotExpectedJson"))


        snapshot_manifest = DatasetReviewItemSnapshotManifest.from_dict(d.pop("snapshotManifest"))




        status = DatasetReviewItemStatus(d.pop("status"))




        def _parse_current_expected_json(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        current_expected_json = _parse_current_expected_json(d.pop("currentExpectedJson"))


        field_decisions = DatasetReviewItemFieldDecisions.from_dict(d.pop("fieldDecisions"))




        def _parse_current_expected_files(data: object) -> list[DatasetReviewExpectedFile] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                current_expected_files_type_0 = []
                _current_expected_files_type_0 = data
                for current_expected_files_type_0_item_data in (_current_expected_files_type_0):
                    current_expected_files_type_0_item = DatasetReviewExpectedFile.from_dict(current_expected_files_type_0_item_data)



                    current_expected_files_type_0.append(current_expected_files_type_0_item)

                return current_expected_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatasetReviewExpectedFile] | None, data)

        current_expected_files = _parse_current_expected_files(d.pop("currentExpectedFiles"))


        file_decisions = DatasetReviewItemFileDecisions.from_dict(d.pop("fileDecisions"))




        input_drifted = d.pop("inputDrifted")

        def _parse_updated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_by = _parse_updated_by(d.pop("updatedBy"))


        updated_at = d.pop("updatedAt")

        dataset_review_item = cls(
            id=id,
            review_id=review_id,
            example_name=example_name,
            snapshot_input_json=snapshot_input_json,
            snapshot_expected_json=snapshot_expected_json,
            snapshot_manifest=snapshot_manifest,
            status=status,
            current_expected_json=current_expected_json,
            field_decisions=field_decisions,
            current_expected_files=current_expected_files,
            file_decisions=file_decisions,
            input_drifted=input_drifted,
            updated_by=updated_by,
            updated_at=updated_at,
        )

        return dataset_review_item
