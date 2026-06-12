from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_start_body_files_additional_property_type_0 import RunStartBodyFilesAdditionalPropertyType0
  from ..models.run_start_body_files_additional_property_type_1_item import RunStartBodyFilesAdditionalPropertyType1Item





T = TypeVar("T", bound="RunStartBodyFiles")



@_attrs_define
class RunStartBodyFiles:
    """ File inputs as references (`{ fileId, filename?, mimeType? }`). Upload bytes via multipart `files.<fieldName>` parts
    instead.

     """

    additional_properties: dict[str, list[RunStartBodyFilesAdditionalPropertyType1Item] | RunStartBodyFilesAdditionalPropertyType0] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_body_files_additional_property_type_0 import RunStartBodyFilesAdditionalPropertyType0
        from ..models.run_start_body_files_additional_property_type_1_item import RunStartBodyFilesAdditionalPropertyType1Item

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():

            if isinstance(prop, RunStartBodyFilesAdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = []
                for additional_property_type_1_item_data in prop:
                    additional_property_type_1_item = additional_property_type_1_item_data.to_dict()
                    field_dict[prop_name].append(additional_property_type_1_item)





        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_body_files_additional_property_type_0 import RunStartBodyFilesAdditionalPropertyType0
        from ..models.run_start_body_files_additional_property_type_1_item import RunStartBodyFilesAdditionalPropertyType1Item
        d = dict(src_dict)
        run_start_body_files = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> list[RunStartBodyFilesAdditionalPropertyType1Item] | RunStartBodyFilesAdditionalPropertyType0:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = RunStartBodyFilesAdditionalPropertyType0.from_dict(data)



                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, list):
                    raise TypeError()
                additional_property_type_1 = []
                _additional_property_type_1 = data
                for additional_property_type_1_item_data in (_additional_property_type_1):
                    additional_property_type_1_item = RunStartBodyFilesAdditionalPropertyType1Item.from_dict(additional_property_type_1_item_data)



                    additional_property_type_1.append(additional_property_type_1_item)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        run_start_body_files.additional_properties = additional_properties
        return run_start_body_files

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[RunStartBodyFilesAdditionalPropertyType1Item] | RunStartBodyFilesAdditionalPropertyType0:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[RunStartBodyFilesAdditionalPropertyType1Item] | RunStartBodyFilesAdditionalPropertyType0) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
