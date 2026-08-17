# react-agent-from-scratch

A ReAct (Reasoning + Acting) agent built in plain Python — no LangChain, no LlamaIndex, no agent framework. Built to understand the actual mechanics behind agent frameworks before using one.

## What is ReAct?

ReAct interleaves reasoning and tool use: instead of answering directly, the LLM outputs a Thought, decides on an Action, receives an Observation from a tool, and repeats until it has enough information to give a final Answer.

Paper: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)

## Tools

- **calculator** — evaluates math expressions
- **wikipedia** — returns a summary from Wikipedia for general knowledge questions
- **rag_search** — queries a separately containerized RAG service ([rag-from-scratch-fastapi](#)) over uploaded documents, and returns a grounded answer

## Architecture

- `agent.py` — `Agent` class: manages conversation state (`messages`) and Groq API calls
- `agent_loop.py` — the ReAct control loop: parses model output, dispatches tool calls, decides when to stop
- `llm.py` — thin Groq client wrapper
- `tools.py` — tool registry (`TOOLS` dict mapping tool name → function)
- `rag_tool.py` — HTTP client for the RAG service's `/ask` endpoint
- `prompts.py` — system prompt defining the ReAct format and available tools


`rag_search` requires the RAG service running separately on `http://localhost:8000` — see that repo's README for setup.

## Example trace
Thought: To answer this question, I need to search the uploaded document for information related to Pakistan's eastern border security situation.


Action: rag_search: What is the security situation on Pakistan's eastern border?
PAUSE


Observation: According to the context, on its eastern front, Pakistan is confronted with a larger and hostile neighbour, India, with a history of major wars and a legacy of unresolved issues.


Answer: The security situation on Pakistan's eastern border is tense, shaped by a long history of conflict with India and unresolved disputes such as Kashmir.
