from graph.state import AgentState
from rag.vectorstore import load_vectorstore


def retriever_agent(state: AgentState) -> AgentState:
    query = state["user_input"]
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(query, k=3)
    retrieved_docs = [doc.page_content for doc in docs]

    return {
        **state,
        "retrieved_docs": retrieved_docs,
    }
