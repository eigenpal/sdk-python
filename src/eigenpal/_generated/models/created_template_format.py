from enum import Enum

class CreatedTemplateFormat(str, Enum):
    DOCX = "docx"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
