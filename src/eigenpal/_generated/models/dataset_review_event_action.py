from enum import Enum

class DatasetReviewEventAction(str, Enum):
    APPROVED = "approved"
    COMMENTED = "commented"
    CREATED = "created"
    EDITED = "edited"
    FIELD_DECISION = "field-decision"
    REJECTED = "rejected"
    REOPENED = "reopened"

    def __str__(self) -> str:
        return str(self.value)
