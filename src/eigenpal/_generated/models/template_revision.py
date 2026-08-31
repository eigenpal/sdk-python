from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TemplateRevision")



@_attrs_define
class TemplateRevision:
    """
        Attributes:
            id (str): Immutable template revision id (tmpr_…).
            number (int):
            sha256 (str):
            created_at (str):
     """

    id: str
    number: int
    sha256: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        sha256 = self.sha256

        created_at: str
        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "number": number,
            "sha256": sha256,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        sha256 = d.pop("sha256")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        template_revision = cls(
            id=id,
            number=number,
            sha256=sha256,
            created_at=created_at,
        )

        return template_revision
