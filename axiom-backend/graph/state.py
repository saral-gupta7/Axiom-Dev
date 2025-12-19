from typing import TypedDict, List


class AgentState(TypedDict):
    user_input: str
    plan: List[str]
    retrieved_docs: List[str]
    critique: str
