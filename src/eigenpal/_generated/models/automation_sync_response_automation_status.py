from enum import Enum

class AutomationSyncResponseAutomationStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    def __str__(self) -> str:
        return str(self.value)
