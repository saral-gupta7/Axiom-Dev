from typing import TypedDict, List


class AgentState(TypedDict):
    user_input: str
    plan: List[str]
    critique: str
