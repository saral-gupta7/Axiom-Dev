# import langgraphs methods for orchestrations
from langgraph.graph import StateGraph, END


#  Bring in the state and existing agents to orchestrate them.
from graph.state import AgentState
from agents.critic import critic_agent
from agents.planner import planner_agent


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("critic", critic_agent)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "critic")
    graph.add_edge("critic", END)

    return graph.compile()


# This tells langgraph, all agents will accept and return agentState
# o
