from enum import Enum

class CreateEmailServerRequestType1Security(str, Enum):
    NONE = "none"
    STARTTLS = "starttls"
    TLS = "tls"

    def __str__(self) -> str:
        return str(self.value)
