from enum import Enum

class HumanReviewTaskDetailStatus(str, Enum):
    APPROVED = "approved"
    CANCELLED = "cancelled"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
