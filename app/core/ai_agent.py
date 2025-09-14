from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from app.config.settings import settings


def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    # Initialize LLM
    llm = ChatGroq(model=llm_id)

    # Add tools if allowed
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Create agent (no state_modifier anymore)
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )

    # Properly structure messages: system + user
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]

    # Run the agent
    response = agent.invoke({"messages": messages})

    # Extract AI responses only
    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response generated."
