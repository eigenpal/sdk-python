from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_task_detail_field_metadata_additional_property_confidence_type_1 import HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1
from ..models.human_review_task_detail_field_metadata_additional_property_review import HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.human_review_task_detail_field_metadata_additional_property_display import HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay





T = TypeVar("T", bound="HumanReviewTaskDetailFieldMetadataAdditionalProperty")



@_attrs_define
class HumanReviewTaskDetailFieldMetadataAdditionalProperty:
    """
        Attributes:
            confidence (float | HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1 | str | Unset):
                Producer-supplied confidence: 0–1 numeric (legacy) or categorical low|medium|high from ai.extract grounding. Not
                calibrated by Eigenpal.
            label (str | Unset): Short label shown in the review UI
            description (str | Unset): Longer reviewer guidance for this field
            review (HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview | Unset): Legacy per-field override kept for
                existing tasks. Prefer selection.fields.review. Default:
                HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview.AUTO.
            display (HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay | Unset): Opaque display metadata preserved
                for the review UI
     """

    confidence: float | HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1 | str | Unset = UNSET
    label: str | Unset = UNSET
    description: str | Unset = UNSET
    review: HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview | Unset = HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview.AUTO
    display: HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.human_review_task_detail_field_metadata_additional_property_display import HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay
        confidence: float | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        elif isinstance(self.confidence, HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1):
            confidence = self.confidence.value
        else:
            confidence = self.confidence

        label = self.label

        description = self.description

        review: str | Unset = UNSET
        if not isinstance(self.review, Unset):
            review = self.review.value


        display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if review is not UNSET:
            field_dict["review"] = review
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_review_task_detail_field_metadata_additional_property_display import HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay
        d = dict(src_dict)
        def _parse_confidence(data: object) -> float | HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_1 = HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1(data)



                return confidence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | HumanReviewTaskDetailFieldMetadataAdditionalPropertyConfidenceType1 | str | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))


        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _review = d.pop("review", UNSET)
        review: HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview | Unset
        if isinstance(_review,  Unset):
            review = UNSET
        else:
            review = HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview(_review)




        _display = d.pop("display", UNSET)
        display: HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay | Unset
        if isinstance(_display,  Unset):
            display = UNSET
        else:
            display = HumanReviewTaskDetailFieldMetadataAdditionalPropertyDisplay.from_dict(_display)




        human_review_task_detail_field_metadata_additional_property = cls(
            confidence=confidence,
            label=label,
            description=description,
            review=review,
            display=display,
        )

        return human_review_task_detail_field_metadata_additional_property
