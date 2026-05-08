from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.api_error_issue import ApiErrorIssue





T = TypeVar("T", bound="ApiErrorEnvelope")



@_attrs_define
class ApiErrorEnvelope:
    """ 
        Attributes:
            issues (list[ApiErrorIssue]):
            request_id (str): Request id echoed via the x-request-id header
            hint (str | Unset): Suggested fix for known error patterns
            docs_url (str | Unset): Link to relevant docs
     """

    issues: list[ApiErrorIssue]
    request_id: str
    hint: str | Unset = UNSET
    docs_url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error_issue import ApiErrorIssue
        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)



        request_id = self.request_id

        hint = self.hint

        docs_url = self.docs_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issues": issues,
            "requestId": request_id,
        })
        if hint is not UNSET:
            field_dict["hint"] = hint
        if docs_url is not UNSET:
            field_dict["docsUrl"] = docs_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error_issue import ApiErrorIssue
        d = dict(src_dict)
        issues = []
        _issues = d.pop("issues")
        for issues_item_data in (_issues):
            issues_item = ApiErrorIssue.from_dict(issues_item_data)



            issues.append(issues_item)


        request_id = d.pop("requestId")

        hint = d.pop("hint", UNSET)

        docs_url = d.pop("docsUrl", UNSET)

        api_error_envelope = cls(
            issues=issues,
            request_id=request_id,
            hint=hint,
            docs_url=docs_url,
        )

        return api_error_envelope

