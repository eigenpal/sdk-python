from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.schema_0 import Schema0





T = TypeVar("T", bound="SourceLockfileResponse")



@_attrs_define
class SourceLockfileResponse:
    """ 
        Attributes:
            lockfile_version (Literal[1]):
            eigenpal_version (str):
            input_hash (str):
            root (Schema0):
     """

    lockfile_version: Literal[1]
    eigenpal_version: str
    input_hash: str
    root: Schema0





    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_0 import Schema0
        lockfile_version = self.lockfile_version

        eigenpal_version = self.eigenpal_version

        input_hash = self.input_hash

        root = self.root.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lockfileVersion": lockfile_version,
            "eigenpalVersion": eigenpal_version,
            "inputHash": input_hash,
            "root": root,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_0 import Schema0
        d = dict(src_dict)
        lockfile_version = cast(Literal[1] , d.pop("lockfileVersion"))
        if lockfile_version != 1:
            raise ValueError(f"lockfileVersion must match const 1, got '{lockfile_version}'")

        eigenpal_version = d.pop("eigenpalVersion")

        input_hash = d.pop("inputHash")

        root = Schema0.from_dict(d.pop("root"))




        source_lockfile_response = cls(
            lockfile_version=lockfile_version,
            eigenpal_version=eigenpal_version,
            input_hash=input_hash,
            root=root,
        )

        return source_lockfile_response

