from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_example_mutation_input_type_0 import DatasetExampleMutationInputType0
  from ..models.dataset_example_mutation_metadata_type_0 import DatasetExampleMutationMetadataType0
  from ..models.dataset_example_mutation_overrides_type_0 import DatasetExampleMutationOverridesType0





T = TypeVar("T", bound="DatasetExampleMutation")



@_attrs_define
class DatasetExampleMutation:
    """
        Attributes:
            name (None | str | Unset):
            input_ (DatasetExampleMutationInputType0 | None | Unset):
            expected (Any | None | Unset):
            metadata (DatasetExampleMutationMetadataType0 | None | Unset):
            annotation (None | str | Unset):
            row_order (int | None | Unset):
            overrides (DatasetExampleMutationOverridesType0 | None | Unset):
     """

    name: None | str | Unset = UNSET
    input_: DatasetExampleMutationInputType0 | None | Unset = UNSET
    expected: Any | None | Unset = UNSET
    metadata: DatasetExampleMutationMetadataType0 | None | Unset = UNSET
    annotation: None | str | Unset = UNSET
    row_order: int | None | Unset = UNSET
    overrides: DatasetExampleMutationOverridesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_example_mutation_input_type_0 import DatasetExampleMutationInputType0
        from ..models.dataset_example_mutation_metadata_type_0 import DatasetExampleMutationMetadataType0
        from ..models.dataset_example_mutation_overrides_type_0 import DatasetExampleMutationOverridesType0
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        input_: dict[str, Any] | None | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, DatasetExampleMutationInputType0):
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
        elif isinstance(self.metadata, DatasetExampleMutationMetadataType0):
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
        elif isinstance(self.overrides, DatasetExampleMutationOverridesType0):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.dataset_example_mutation_input_type_0 import DatasetExampleMutationInputType0
        from ..models.dataset_example_mutation_metadata_type_0 import DatasetExampleMutationMetadataType0
        from ..models.dataset_example_mutation_overrides_type_0 import DatasetExampleMutationOverridesType0
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_input_(data: object) -> DatasetExampleMutationInputType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = DatasetExampleMutationInputType0.from_dict(data)



                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleMutationInputType0 | None | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))


        def _parse_expected(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        def _parse_metadata(data: object) -> DatasetExampleMutationMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DatasetExampleMutationMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleMutationMetadataType0 | None | Unset, data)

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


        def _parse_overrides(data: object) -> DatasetExampleMutationOverridesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = DatasetExampleMutationOverridesType0.from_dict(data)



                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetExampleMutationOverridesType0 | None | Unset, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))


        dataset_example_mutation = cls(
            name=name,
            input_=input_,
            expected=expected,
            metadata=metadata,
            annotation=annotation,
            row_order=row_order,
            overrides=overrides,
        )


        dataset_example_mutation.additional_properties = d
        return dataset_example_mutation

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
