from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph.state import AgentState
from graph.graph import build_graph

from pydantic import BaseModel
from typing import cast

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
graph = build_graph()


class RunRequest(BaseModel):
    prompt: str


@app.post("/run")
def agent_testing(req: RunRequest):
    initial_state = cast(AgentState, {"user_input": req.prompt})

    final_state = graph.invoke(initial_state)

    return final_state
