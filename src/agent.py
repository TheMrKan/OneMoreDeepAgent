import os
import json
from pathlib import Path
from loguru import logger
from deepagents import create_deep_agent
from deepagents.backends import LocalShellBackend
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient


async def create_agent():
    model = ChatOpenAI(
        model=os.environ["PROVIDER_MODEL"],
        base_url=os.environ["PROVIDER_URL"],
        api_key=os.environ["PROVIDER_API_KEY"],
    )

    backend = LocalShellBackend(
        os.environ["WORKSPACE_PATH"],
        virtual_mode=True
    )

    try:
       mcp_tools = await __get_mcp_tools()
       logger.info(f"Loaded {len(mcp_tools)} MCP tools")
    except Exception as e:
        logger.exception("Failed to load MCP tools", exc_info=e)
        mcp_tools = []

    agent = create_deep_agent(
        model=model,
        checkpointer=MemorySaver(),
        backend=backend,
        tools=mcp_tools,
    )

    return agent


async def __get_mcp_tools() -> list:
    with open(Path(__file__).parent.parent / "mcp.json", encoding="utf-8") as f:
        config = json.load(f)

    mcp_client = MultiServerMCPClient(config)
    return await mcp_client.get_tools()
