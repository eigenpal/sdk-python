from enum import Enum

class RunReviewStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    WONT_FIX = "wont_fix"

    def __str__(self) -> str:
        return str(self.value)
