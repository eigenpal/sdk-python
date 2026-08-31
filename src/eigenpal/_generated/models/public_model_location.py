from enum import Enum

class PublicModelLocation(str, Enum):
    HOSTED = "hosted"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
