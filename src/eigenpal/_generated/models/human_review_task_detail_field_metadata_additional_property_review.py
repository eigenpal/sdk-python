from enum import Enum

class HumanReviewTaskDetailFieldMetadataAdditionalPropertyReview(str, Enum):
    ALWAYS = "always"
    AUTO = "auto"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
