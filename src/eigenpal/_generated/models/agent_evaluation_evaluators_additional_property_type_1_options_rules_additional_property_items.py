from enum import Enum

class AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems(str, Enum):
    AT_LEAST = "at-least"
    AT_MOST = "at-most"
    EXACTLY = "exactly"

    def __str__(self) -> str:
        return str(self.value)
