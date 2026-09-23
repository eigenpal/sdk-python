from enum import Enum

class DatasetReviewExpectedFileOrigin(str, Enum):
    CORRECTED = "corrected"
    SNAPSHOT = "snapshot"
    UPLOADED = "uploaded"

    def __str__(self) -> str:
        return str(self.value)
