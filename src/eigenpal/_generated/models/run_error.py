from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunError")



@_attrs_define
class RunError:
    """
        Attributes:
            code (str): Machine-readable failure code. Do not branch on message text.
            message (str): Human-readable failure explanation.
            retryable (bool): Whether another attempt might succeed. Does not schedule a retry.
            status_code (int | Unset): HTTP-style business code configured by control.fail, not the API response status.
                Absent for untyped failures.
            step (str | Unset): Name of the control.fail step that rejected the run, when known.
     """

    code: str
    message: str
    retryable: bool
    status_code: int | Unset = UNSET
    step: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        retryable = self.retryable

        status_code = self.status_code

        step = self.step


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "message": message,
            "retryable": retryable,
        })
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        retryable = d.pop("retryable")

        status_code = d.pop("statusCode", UNSET)

        step = d.pop("step", UNSET)

        run_error = cls(
            code=code,
            message=message,
            retryable=retryable,
            status_code=status_code,
            step=step,
        )

        return run_error
