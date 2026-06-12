from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_error_issue_severity import ApiErrorIssueSeverity






T = TypeVar("T", bound="ApiErrorIssue")



@_attrs_define
class ApiErrorIssue:
    """
        Attributes:
            field (str): JSON path of the offending field, or "<root>"
            message (str): Human-readable error message
            code (str): Machine-readable error code (e.g. invalid_value, not_found)
            severity (ApiErrorIssueSeverity): Issue severity
     """

    field: str
    message: str
    code: str
    severity: ApiErrorIssueSeverity





    def to_dict(self) -> dict[str, Any]:
        field = self.field

        message = self.message

        code = self.code

        severity = self.severity.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "field": field,
            "message": message,
            "code": code,
            "severity": severity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        message = d.pop("message")

        code = d.pop("code")

        severity = ApiErrorIssueSeverity(d.pop("severity"))




        api_error_issue = cls(
            field=field,
            message=message,
            code=code,
            severity=severity,
        )

        return api_error_issue
