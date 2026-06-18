from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_usage import RunUsage





T = TypeVar("T", bound="RunUsageResponse")



@_attrs_define
class RunUsageResponse:
    """
        Attributes:
            usage (None | RunUsage):
     """

    usage: None | RunUsage





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_usage import RunUsage
        usage: dict[str, Any] | None
        if isinstance(self.usage, RunUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "usage": usage,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_usage import RunUsage
        d = dict(src_dict)
        def _parse_usage(data: object) -> None | RunUsage:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = RunUsage.from_dict(data)



                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunUsage, data)

        usage = _parse_usage(d.pop("usage"))


        run_usage_response = cls(
            usage=usage,
        )

        return run_usage_response
