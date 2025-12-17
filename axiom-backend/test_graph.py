from typing import cast
from graph.graph import build_graph
from graph.state import AgentState


graph = build_graph()


initial_state = cast(AgentState, {"user_input": "Make a URL shortener in FastAPI"})

final_state = graph.invoke(initial_state)

print("\n--- FINAL STATE ---\n")
print(final_state)
