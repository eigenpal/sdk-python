from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="DatasetImportResponseType0")



@_attrs_define
class DatasetImportResponseType0:
    """
        Attributes:
            mode (Literal['append']):
            created (int):
            expected_set (int):
            skipped (int):
            issues (list[Any]):
     """

    mode: Literal['append']
    created: int
    expected_set: int
    skipped: int
    issues: list[Any]





    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        created = self.created

        expected_set = self.expected_set

        skipped = self.skipped

        issues = self.issues




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mode": mode,
            "created": created,
            "expectedSet": expected_set,
            "skipped": skipped,
            "issues": issues,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal['append'] , d.pop("mode"))
        if mode != 'append':
            raise ValueError(f"mode must match const 'append', got '{mode}'")

        created = d.pop("created")

        expected_set = d.pop("expectedSet")

        skipped = d.pop("skipped")

        issues = cast(list[Any], d.pop("issues"))


        dataset_import_response_type_0 = cls(
            mode=mode,
            created=created,
            expected_set=expected_set,
            skipped=skipped,
            issues=issues,
        )

        return dataset_import_response_type_0
