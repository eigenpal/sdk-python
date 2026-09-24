from enum import Enum

class DatasetReviewInboxItemStatus(str, Enum):
    CANCELLED = "cancelled"
    CLOSED = "closed"
    DRAFT = "draft"
    OPEN = "open"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
