from typing import cast
from graph.state import AgentState
from agents.planner import planner_agent

initial_state = cast(AgentState, {"user_input": "Build a URL shortener using FastAPI"})

new_state = planner_agent(initial_state)
