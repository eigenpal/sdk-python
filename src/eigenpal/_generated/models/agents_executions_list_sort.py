from enum import Enum

class AgentsExecutionsListSort(str, Enum):
    COMPLETEDAT = "completedAt"
    CREATEDAT = "createdAt"
    EXAMPLENAME = "exampleName"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
