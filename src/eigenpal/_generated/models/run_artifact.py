from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunArtifact")



@_attrs_define
class RunArtifact:
    """
        Attributes:
            name (str):
            path (str): Canonical artifact path for GET /api/v1/runs/:id/artifacts/:path.
            step_name (str | Unset): Workflow step that produced the file, when known.
            content_type (None | str | Unset):
            size (int | None | Unset):
     """

    name: str
    path: str
    step_name: str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    size: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        step_name = self.step_name

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "path": path,
        })
        if step_name is not UNSET:
            field_dict["stepName"] = step_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        step_name = d.pop("stepName", UNSET)

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))


        run_artifact = cls(
            name=name,
            path=path,
            step_name=step_name,
            content_type=content_type,
            size=size,
        )

        return run_artifact
