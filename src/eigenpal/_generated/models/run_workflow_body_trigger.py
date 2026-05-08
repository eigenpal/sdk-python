from enum import Enum

class RunWorkflowBodyTrigger(str, Enum):
    API = "api"
    CLI = "cli"

    def __str__(self) -> str:
        return str(self.value)
