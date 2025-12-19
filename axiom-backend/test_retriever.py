from typing import cast
from agents.retriever import retriever_agent
from graph.state import AgentState

initial_state = cast(AgentState, {"user_input": "Build a backend API using FastAPI"})

new_state = retriever_agent(initial_state)

print("\n--- RETRIEVED DOCS ---\n")
for doc in new_state["retrieved_docs"]:
    print("-", doc)
