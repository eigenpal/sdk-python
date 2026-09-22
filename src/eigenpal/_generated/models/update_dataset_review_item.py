from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_dataset_review_item_action import UpdateDatasetReviewItemAction
from ..models.update_dataset_review_item_decision_type_0 import UpdateDatasetReviewItemDecisionType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateDatasetReviewItem")



@_attrs_define
class UpdateDatasetReviewItem:
    """
        Attributes:
            action (UpdateDatasetReviewItemAction):
            expected_updated_at (str): ISO timestamp of the item `updatedAt` the client last observed. Required for
                optimistic concurrency.
            expected (Any | Unset):
            comment (None | str | Unset):
            field_path (None | str | Unset):
            decision (None | Unset | UpdateDatasetReviewItemDecisionType0):
     """

    action: UpdateDatasetReviewItemAction
    expected_updated_at: str
    expected: Any | Unset = UNSET
    comment: None | str | Unset = UNSET
    field_path: None | str | Unset = UNSET
    decision: None | Unset | UpdateDatasetReviewItemDecisionType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        expected_updated_at = self.expected_updated_at

        expected = self.expected

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_path: None | str | Unset
        if isinstance(self.field_path, Unset):
            field_path = UNSET
        else:
            field_path = self.field_path

        decision: None | str | Unset
        if isinstance(self.decision, Unset):
            decision = UNSET
        elif isinstance(self.decision, UpdateDatasetReviewItemDecisionType0):
            decision = self.decision.value
        else:
            decision = self.decision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "expectedUpdatedAt": expected_updated_at,
        })
        if expected is not UNSET:
            field_dict["expected"] = expected
        if comment is not UNSET:
            field_dict["comment"] = comment
        if field_path is not UNSET:
            field_dict["fieldPath"] = field_path
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = UpdateDatasetReviewItemAction(d.pop("action"))




        expected_updated_at = d.pop("expectedUpdatedAt")

        expected = d.pop("expected", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_field_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_path = _parse_field_path(d.pop("fieldPath", UNSET))


        def _parse_decision(data: object) -> None | Unset | UpdateDatasetReviewItemDecisionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decision_type_0 = UpdateDatasetReviewItemDecisionType0(data)



                return decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateDatasetReviewItemDecisionType0, data)

        decision = _parse_decision(d.pop("decision", UNSET))


        update_dataset_review_item = cls(
            action=action,
            expected_updated_at=expected_updated_at,
            expected=expected,
            comment=comment,
            field_path=field_path,
            decision=decision,
        )


        update_dataset_review_item.additional_properties = d
        return update_dataset_review_item

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
