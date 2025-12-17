from langchain_openai import ChatOpenAI
from graph.state import AgentState
from langchain_core.messages import HumanMessage
from config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=OPENAI_API_KEY)


def critic_agent(state: AgentState) -> AgentState:
    plan = state["plan"]
    plan_text = "\n".join(plan)

    prompt = (
        "You are a senior software reviewer.\n\n"
        "You are supposed to meticulously review this plan and suggest technical risks, Suggested Improvements, or missing parts of the plan.\n"
        "Here is the development plan:\n"
        f"Plan: {plan_text}\n\n"
        "Respond with a concise critique."
    )

    response = llm.invoke([HumanMessage(content=prompt)])
    critique = response.content.strip()

    return {**state, "critique": critique}
