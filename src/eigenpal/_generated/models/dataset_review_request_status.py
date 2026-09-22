from enum import Enum

class DatasetReviewRequestStatus(str, Enum):
    CLOSED = "closed"
    DRAFT = "draft"
    OPEN = "open"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
