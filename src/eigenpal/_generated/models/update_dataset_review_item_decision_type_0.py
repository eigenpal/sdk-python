from enum import Enum

class UpdateDatasetReviewItemDecisionType0(str, Enum):
    APPROVED = "approved"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
