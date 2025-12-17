from fastapi import FastAPI

from graph.state import AgentState
from graph.graph import build_graph

from pydantic import BaseModel
from typing import cast


app = FastAPI()

graph = build_graph()


class RunRequest(BaseModel):
    prompt: str


@app.post("/run")
def agent_testing(req: RunRequest):
    initial_state = cast(AgentState, {"user_input": req.prompt})

    final_state = graph.invoke(initial_state)

    return final_state
