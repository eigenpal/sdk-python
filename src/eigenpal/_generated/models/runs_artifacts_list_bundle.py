from enum import Enum

class RunsArtifactsListBundle(str, Enum):
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
