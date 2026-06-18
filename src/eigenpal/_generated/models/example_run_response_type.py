from enum import Enum

class ExampleRunResponseType(str, Enum):
    AGENT = "agent"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
