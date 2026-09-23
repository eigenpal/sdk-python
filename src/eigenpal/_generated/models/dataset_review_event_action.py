from enum import Enum

class DatasetReviewEventAction(str, Enum):
    APPROVED = "approved"
    COMMENTED = "commented"
    CREATED = "created"
    EDITED = "edited"
    FIELD_DECISION = "field-decision"
    FILE_DECISION = "file-decision"
    FILE_EDITED = "file-edited"
    REMOVED = "removed"
    REOPENED = "reopened"

    def __str__(self) -> str:
        return str(self.value)
