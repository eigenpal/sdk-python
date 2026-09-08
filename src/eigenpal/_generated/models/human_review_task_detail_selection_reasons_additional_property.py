from enum import Enum

class HumanReviewTaskDetailSelectionReasonsAdditionalProperty(str, Enum):
    ALL = "all"
    ALWAYS = "always"
    EXCLUDED = "excluded"
    EXPLICIT = "explicit"
    LOW_CONFIDENCE = "low_confidence"
    MISSING_CONFIDENCE = "missing_confidence"
    MISSING_CONFIDENCE_SKIP = "missing_confidence_skip"
    NEVER = "never"
    REVIEWER_EDIT = "reviewer_edit"
    THRESHOLD_MET = "threshold_met"
    UNMATCHED = "unmatched"

    def __str__(self) -> str:
        return str(self.value)
