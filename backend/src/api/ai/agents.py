from langgraph.prebuilt import create_react_agent
from api.ai.llms import get_openai_llm
from api.ai.assistants import EMAIL_TOOLS


def get_email_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=list(EMAIL_TOOLS.values()),
        prompt="You're a helpful assistant for managing my email inbox for generating, sending, and reviewing emails"
        )

    return agent