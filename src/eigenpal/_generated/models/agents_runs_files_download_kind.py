from enum import Enum

class AgentsRunsFilesDownloadKind(str, Enum):
    INPUT = "input"
    ISSUES = "issues"
    LOCKFILE = "lockfile"
    OUTPUT = "output"
    TRACE = "trace"

    def __str__(self) -> str:
        return str(self.value)
