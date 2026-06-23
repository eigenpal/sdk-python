from enum import Enum

class RunReviewRequestStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    WONT_FIX = "wont_fix"

    def __str__(self) -> str:
        return str(self.value)
