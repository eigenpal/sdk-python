from enum import Enum

class RunType(str, Enum):
    AGENT = "agent"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
