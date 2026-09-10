from enum import Enum

class FolderType(str, Enum):
    TEMPLATE = "template"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
