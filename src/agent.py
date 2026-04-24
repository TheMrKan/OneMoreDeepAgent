import os
from deepagents import create_deep_agent
from deepagents.backends import LocalShellBackend
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver


def create_agent():
    model = ChatOpenAI(
        model=os.environ["PROVIDER_MODEL"],
        base_url=os.environ["PROVIDER_URL"],
        api_key=os.environ["PROVIDER_API_KEY"],
    )

    backend = LocalShellBackend(
        os.environ["WORKSPACE_PATH"],
        virtual_mode=True
    )

    agent = create_deep_agent(
        model=model,
        checkpointer=MemorySaver(),
        backend=backend
    )

    return agent
