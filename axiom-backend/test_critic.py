from typing import cast
from agents.critic import critic_agent
from graph.state import AgentState

initial_state = cast(
    AgentState,
    {
        "user_input": "Build a URL shortener using FastAPI",
        "plan": [
            "Define requirements",
            "Design database schema",
            "Implement API endpoints",
            "Deploy application",
        ],
    },
)

new_state = critic_agent(initial_state)
print(new_state["critique"])
