from enum import Enum

class HumanReviewTaskDetailSourceKind(str, Enum):
    AGENT_TOOL = "agent_tool"
    WORKFLOW_STEP = "workflow_step"

    def __str__(self) -> str:
        return str(self.value)
