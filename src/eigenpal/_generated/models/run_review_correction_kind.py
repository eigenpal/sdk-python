from enum import Enum

class RunReviewCorrectionKind(str, Enum):
    FIELD = "field"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
