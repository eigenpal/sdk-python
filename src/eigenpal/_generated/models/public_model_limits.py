from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PublicModelLimits")



@_attrs_define
class PublicModelLimits:
    """
        Attributes:
            request_timeout_seconds (int | Unset):
            max_concurrent_requests (int | Unset):
     """

    request_timeout_seconds: int | Unset = UNSET
    max_concurrent_requests: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        request_timeout_seconds = self.request_timeout_seconds

        max_concurrent_requests = self.max_concurrent_requests


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if request_timeout_seconds is not UNSET:
            field_dict["requestTimeoutSeconds"] = request_timeout_seconds
        if max_concurrent_requests is not UNSET:
            field_dict["maxConcurrentRequests"] = max_concurrent_requests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_timeout_seconds = d.pop("requestTimeoutSeconds", UNSET)

        max_concurrent_requests = d.pop("maxConcurrentRequests", UNSET)

        public_model_limits = cls(
            request_timeout_seconds=request_timeout_seconds,
            max_concurrent_requests=max_concurrent_requests,
        )

        return public_model_limits
