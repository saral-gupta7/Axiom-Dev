from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from graph.state import AgentState
from config import OPENAI_API_KEY


llm = ChatOpenAI(temperature=0.2, model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def planner_agent(state: AgentState) -> AgentState:
    task = state["user_input"]
    prompt = (
        "You are a senior software architect.\n\n"
        "Break the following task into clear, ordered development steps.\n\n"
        f"TASK:\n{task}\n\n"
        "Return a numbered list."
    )

    response = llm.invoke([HumanMessage(content=prompt)])

    steps = [step.strip() for step in response.content.split("\n") if step.strip()]
    return {
        **state,
        "plan": steps,
    }
