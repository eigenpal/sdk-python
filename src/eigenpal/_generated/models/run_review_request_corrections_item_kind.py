from enum import Enum

class RunReviewRequestCorrectionsItemKind(str, Enum):
    FIELD = "field"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
