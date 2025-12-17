# Axiom Dev 🧠⚙️

**Agentic AI Backend for Structured Software Planning**

Axiom Dev is an agentic AI system that transforms a raw software idea into a structured development plan using multiple collaborating agents orchestrated with LangGraph and exposed via FastAPI.

Instead of a single LLM call, Axiom Dev decomposes reasoning into independent, testable agents that communicate through a shared state.

---

## ✨ Key Features

- 🧩 **Agentic architecture** using LangGraph
- 🧠 **Planner Agent** – breaks user ideas into ordered development steps
- 🔍 **Critic Agent** – reviews plans for risks, missing steps, and improvements
- 🔄 **Shared typed state** passed safely across agents
- 🚀 **FastAPI backend** with a clean `/run` endpoint
- 🧪 **Agents are independently testable and composable**

---

## 🏗️ Architecture Overview

```
User Prompt
   ↓
Planner Agent
   ↓
Critic Agent
   ↓
Final Structured Output
```

Each agent:

- Reads from shared state
- Performs one responsibility
- Returns an updated state

LangGraph orchestrates execution order and termination.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – API layer
- **LangGraph** – agent orchestration
- **LangChain** – LLM abstractions
- **OpenAI** – language models
- **Pydantic** – request validation & typing

---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
pip install fastapi uvicorn langgraph langchain-core langchain-openai python-dotenv
```

### 2️⃣ Set environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 3️⃣ Run the server

```bash
uvicorn main:app --reload
```

---

## 📡 API Usage

### Endpoint

```
POST /run
```

### Request Body

```json
{
  "prompt": "Build a URL shortener using FastAPI"
}
```

### Response

```json
{
  "user_input": "...",
  "plan": [...],
  "critique": "..."
}
```

---

## 🧠 Design Philosophy

- Agents are simple functions
- State is explicit and typed
- Orchestration is separate from intelligence
- Each component is testable in isolation

LangGraph is used strictly for execution flow, not reasoning.

---

## 🔮 Roadmap

- Retriever Agent (RAG with vector database)
- Synthesizer Agent for final outputs
- Frontend (Next.js)
- Metrics & performance logging

---

## 📌 Why Axiom Dev?

This project was built to deeply understand:

- Agentic AI systems
- State-driven orchestration
- Practical LangGraph usage
- Clean backend architecture for AI products

---
