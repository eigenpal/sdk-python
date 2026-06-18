from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="DatasetImportResponseType1")



@_attrs_define
class DatasetImportResponseType1:
    """
        Attributes:
            mode (Literal['replace']):
            created (int):
            expected_set (int):
            deleted (int):
            files_deleted (int):
     """

    mode: Literal['replace']
    created: int
    expected_set: int
    deleted: int
    files_deleted: int





    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        created = self.created

        expected_set = self.expected_set

        deleted = self.deleted

        files_deleted = self.files_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mode": mode,
            "created": created,
            "expectedSet": expected_set,
            "deleted": deleted,
            "filesDeleted": files_deleted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal['replace'] , d.pop("mode"))
        if mode != 'replace':
            raise ValueError(f"mode must match const 'replace', got '{mode}'")

        created = d.pop("created")

        expected_set = d.pop("expectedSet")

        deleted = d.pop("deleted")

        files_deleted = d.pop("filesDeleted")

        dataset_import_response_type_1 = cls(
            mode=mode,
            created=created,
            expected_set=expected_set,
            deleted=deleted,
            files_deleted=files_deleted,
        )

        return dataset_import_response_type_1
