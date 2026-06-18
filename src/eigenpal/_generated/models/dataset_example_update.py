from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_example_update_input_type_0 import DatasetExampleUpdateInputType0
  from ..models.dataset_example_update_metadata_type_0 import DatasetExampleUpdateMetadataType0
  from ..models.dataset_example_update_overrides_type_0 import DatasetExampleUpdateOverridesType0





T = TypeVar("T", bound="DatasetExampleUpdate")



@_attrs_define
class DatasetExampleUpdate:
    """
        Attributes:
            input_ (DatasetExampleUpdateInputType0 | None | Unset):
            expected (Any | None | Unset):
            metadata (DatasetExampleUpdateMetadataType0 | None | Unset):
            annotation (None | str | Unset):
            row_order (int | None | Unset):
            overrides (DatasetExampleUpdateOverridesType0 | None | Unset):
     """

    input_: DatasetExampleUpdateInputType0 | None | Unset = UNSET
    expected: Any | None | Unset = UNSET
    metadata: DatasetExampleUpdateMetadataType0 | None | Unset = UNSET
    annotation: None | str | Unset = UNSET
    row_order: int | None | Unset = UNSET
    overrides: DatasetExampleUpdateOverridesType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_example_update_input_type_0 import DatasetExampleUpdateInputType0
        from ..models.dataset_example_update_metadata_type_0 import DatasetExampleUpdateMetadataType0
        from ..models.dataset_example_update_overrides_type_0 import DatasetExampleUpdateOverridesType0
        input_: dict[str, Any] | None | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, DatasetExampleUpdateInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        expected: Any | None | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DatasetExampleUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        row_order: int | None | Unset
        if isinstance(self.row_order, Unset):
            row_order = UNSET
        else:
            row_order = self.row_order

        overrides: dict[str, Any] | None | Unset
        if isinstance(self.overrides, Unset):
            overrides = UNSET
        elif isinstance(self.overrides, DatasetExampleUpdateOverridesType0):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if expected is not UNSET:
            field_dict["expected"] = expected
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if row_order is not UNSET:
            field_dict["rowOrder"] = row_order
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_example_update_input_type_0 import DatasetExampleUpdateInputType0
        from ..models.dataset_example_update_metadata_type_0 import DatasetExampleUpdateMetadataType0
        from ..models.dataset_example_update_overrides_type_0 import DatasetExampleUpdateOverridesType0
        d = dict(src_dict)
        def _parse_input_(data: object) -> DatasetExampleUpdateInputType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = DatasetExampleUpdateInputType0.from_dict(data)



                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleUpdateInputType0 | None | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))


        def _parse_expected(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        def _parse_metadata(data: object) -> DatasetExampleUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DatasetExampleUpdateMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))


        def _parse_row_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_order = _parse_row_order(d.pop("rowOrder", UNSET))


        def _parse_overrides(data: object) -> DatasetExampleUpdateOverridesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = DatasetExampleUpdateOverridesType0.from_dict(data)



                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleUpdateOverridesType0 | None | Unset, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))


        dataset_example_update = cls(
            input_=input_,
            expected=expected,
            metadata=metadata,
            annotation=annotation,
            row_order=row_order,
            overrides=overrides,
        )

        return dataset_example_update
