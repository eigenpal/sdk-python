from enum import Enum

class TestEmailServerResponseType0Transport(str, Enum):
    RESEND = "resend"
    SMTP = "smtp"

    def __str__(self) -> str:
        return str(self.value)
