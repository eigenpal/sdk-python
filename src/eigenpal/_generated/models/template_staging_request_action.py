from enum import Enum

class TemplateStagingRequestAction(str, Enum):
    CLEANUP = "cleanup"
    FINALIZE = "finalize"

    def __str__(self) -> str:
        return str(self.value)
