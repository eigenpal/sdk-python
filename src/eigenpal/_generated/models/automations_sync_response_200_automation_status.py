from enum import Enum

class AutomationsSyncResponse200AutomationStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    def __str__(self) -> str:
        return str(self.value)
