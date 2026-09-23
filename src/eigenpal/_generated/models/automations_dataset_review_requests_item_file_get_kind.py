from enum import Enum

class AutomationsDatasetReviewRequestsItemFileGetKind(str, Enum):
    EXPECTED = "expected"
    INPUT = "input"

    def __str__(self) -> str:
        return str(self.value)
