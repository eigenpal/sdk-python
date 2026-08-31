from enum import Enum

class TemplateTokensItemType(str, Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    DATE = "date"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
