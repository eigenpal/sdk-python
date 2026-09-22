from enum import Enum

class DatasetReviewItemStatus(str, Enum):
    APPROVED = "approved"
    EDITED = "edited"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
