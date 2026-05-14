from enum import Enum

class AgentsExecutionsFilesDownloadKind(str, Enum):
    INPUT = "input"
    ISSUES = "issues"
    OUTPUT = "output"
    TRACE = "trace"

    def __str__(self) -> str:
        return str(self.value)
