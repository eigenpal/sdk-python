from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunUsageTokens")



@_attrs_define
class RunUsageTokens:
    """
        Attributes:
            input_ (float | None):
            output (float | None):
            cache_read (float | None):
            cache_write (float | None):
     """

    input_: float | None
    output: float | None
    cache_read: float | None
    cache_write: float | None





    def to_dict(self) -> dict[str, Any]:
        input_: float | None
        input_ = self.input_

        output: float | None
        output = self.output

        cache_read: float | None
        cache_read = self.cache_read

        cache_write: float | None
        cache_write = self.cache_write


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input": input_,
            "output": output,
            "cacheRead": cache_read,
            "cacheWrite": cache_write,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_input_(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        input_ = _parse_input_(d.pop("input"))


        def _parse_output(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        output = _parse_output(d.pop("output"))


        def _parse_cache_read(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cache_read = _parse_cache_read(d.pop("cacheRead"))


        def _parse_cache_write(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cache_write = _parse_cache_write(d.pop("cacheWrite"))


        run_usage_tokens = cls(
            input_=input_,
            output=output,
            cache_read=cache_read,
            cache_write=cache_write,
        )

        return run_usage_tokens
