from enum import Enum

class AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder(str, Enum):
    ORDERED = "ordered"
    UNORDERED = "unordered"

    def __str__(self) -> str:
        return str(self.value)
