from enum import Enum

class CreateDatasetReviewRequestStatus(str, Enum):
    DRAFT = "draft"
    OPEN = "open"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
