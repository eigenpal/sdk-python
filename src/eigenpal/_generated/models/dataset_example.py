from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_type import AutomationType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_example_expected_files_item import DatasetExampleExpectedFilesItem
  from ..models.dataset_example_input_type_0 import DatasetExampleInputType0
  from ..models.dataset_example_metadata_type_0 import DatasetExampleMetadataType0
  from ..models.dataset_example_overrides_type_0 import DatasetExampleOverridesType0





T = TypeVar("T", bound="DatasetExample")



@_attrs_define
class DatasetExample:
    """
        Attributes:
            id (str): Stable public example id. Workflow examples use DB ids; agent examples use deterministic name-derived
                ids.
            name (str):
            automation_id (str):
            automation_type (AutomationType):
            input_ (DatasetExampleInputType0 | None):
            expected (Any | None):
            expected_files (list[DatasetExampleExpectedFilesItem]):
            metadata (DatasetExampleMetadataType0 | None):
            annotation (None | str):
            row_order (float | None):
            overrides (DatasetExampleOverridesType0 | None):
            latest_run_id (None | str):
            created_at (str | Unset):
            updated_at (None | str | Unset):
     """

    id: str
    name: str
    automation_id: str
    automation_type: AutomationType
    input_: DatasetExampleInputType0 | None
    expected: Any | None
    expected_files: list[DatasetExampleExpectedFilesItem]
    metadata: DatasetExampleMetadataType0 | None
    annotation: None | str
    row_order: float | None
    overrides: DatasetExampleOverridesType0 | None
    latest_run_id: None | str
    created_at: str | Unset = UNSET
    updated_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_example_expected_files_item import DatasetExampleExpectedFilesItem
        from ..models.dataset_example_input_type_0 import DatasetExampleInputType0
        from ..models.dataset_example_metadata_type_0 import DatasetExampleMetadataType0
        from ..models.dataset_example_overrides_type_0 import DatasetExampleOverridesType0
        id = self.id

        name = self.name

        automation_id = self.automation_id

        automation_type = self.automation_type.value

        input_: dict[str, Any] | None
        if isinstance(self.input_, DatasetExampleInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        expected: Any | None
        expected = self.expected

        expected_files = []
        for expected_files_item_data in self.expected_files:
            expected_files_item = expected_files_item_data.to_dict()
            expected_files.append(expected_files_item)



        metadata: dict[str, Any] | None
        if isinstance(self.metadata, DatasetExampleMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        annotation: None | str
        annotation = self.annotation

        row_order: float | None
        row_order = self.row_order

        overrides: dict[str, Any] | None
        if isinstance(self.overrides, DatasetExampleOverridesType0):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides

        latest_run_id: None | str
        latest_run_id = self.latest_run_id

        created_at: str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "automationId": automation_id,
            "automationType": automation_type,
            "input": input_,
            "expected": expected,
            "expectedFiles": expected_files,
            "metadata": metadata,
            "annotation": annotation,
            "rowOrder": row_order,
            "overrides": overrides,
            "latestRunId": latest_run_id,
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_example_expected_files_item import DatasetExampleExpectedFilesItem
        from ..models.dataset_example_input_type_0 import DatasetExampleInputType0
        from ..models.dataset_example_metadata_type_0 import DatasetExampleMetadataType0
        from ..models.dataset_example_overrides_type_0 import DatasetExampleOverridesType0
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        automation_id = d.pop("automationId")

        automation_type = AutomationType(d.pop("automationType"))




        def _parse_input_(data: object) -> DatasetExampleInputType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = DatasetExampleInputType0.from_dict(data)



                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleInputType0 | None, data)

        input_ = _parse_input_(d.pop("input"))


        def _parse_expected(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        expected = _parse_expected(d.pop("expected"))


        expected_files = []
        _expected_files = d.pop("expectedFiles")
        for expected_files_item_data in (_expected_files):
            expected_files_item = DatasetExampleExpectedFilesItem.from_dict(expected_files_item_data)



            expected_files.append(expected_files_item)


        def _parse_metadata(data: object) -> DatasetExampleMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DatasetExampleMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))


        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))


        def _parse_row_order(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        row_order = _parse_row_order(d.pop("rowOrder"))


        def _parse_overrides(data: object) -> DatasetExampleOverridesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = DatasetExampleOverridesType0.from_dict(data)



                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleOverridesType0 | None, data)

        overrides = _parse_overrides(d.pop("overrides"))


        def _parse_latest_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_run_id = _parse_latest_run_id(d.pop("latestRunId"))


        def _parse_created_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        dataset_example = cls(
            id=id,
            name=name,
            automation_id=automation_id,
            automation_type=automation_type,
            input_=input_,
            expected=expected,
            expected_files=expected_files,
            metadata=metadata,
            annotation=annotation,
            row_order=row_order,
            overrides=overrides,
            latest_run_id=latest_run_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        return dataset_example
