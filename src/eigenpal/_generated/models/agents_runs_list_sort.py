from enum import Enum

class AgentsRunsListSort(str, Enum):
    COMPLETEDAT = "completedAt"
    CREATEDAT = "createdAt"
    EXAMPLEID = "exampleId"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
