from enum import Enum

class WorkflowsListKind(str, Enum):
    BLOCK = "block"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
