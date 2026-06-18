from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunStartMultipartRequest")



@_attrs_define
class RunStartMultipartRequest:
    """
        Attributes:
            target (str): Automation target, e.g. `workflows.invoice`.
            input_ (str | Unset): JSON-encoded scalar input object.
            overrides (str | Unset): JSON-encoded step overrides.
            metadata (str | Unset): JSON-encoded run metadata.
     """

    target: str
    input_: str | Unset = UNSET
    overrides: str | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target = self.target

        input_ = self.input_

        overrides = self.overrides

        metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target": target,
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("target", (None, str(self.target).encode(), "text/plain")))



        if not isinstance(self.input_, Unset):
            files.append(("input", (None, str(self.input_).encode(), "text/plain")))



        if not isinstance(self.overrides, Unset):
            files.append(("overrides", (None, str(self.overrides).encode(), "text/plain")))



        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target = d.pop("target")

        input_ = d.pop("input", UNSET)

        overrides = d.pop("overrides", UNSET)

        metadata = d.pop("metadata", UNSET)

        run_start_multipart_request = cls(
            target=target,
            input_=input_,
            overrides=overrides,
            metadata=metadata,
        )


        run_start_multipart_request.additional_properties = d
        return run_start_multipart_request

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
