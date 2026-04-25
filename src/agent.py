import asyncio
import os
import json
import datetime
from pathlib import Path
from loguru import logger
from deepagents import create_deep_agent, SubAgent
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

    workspace_path = Path(os.environ["WORKSPACE_PATH"]).resolve()
    backend = LocalShellBackend(
        workspace_path,
        virtual_mode=False
    )

    try:
        mcp_tools = await __get_mcp_tools()
        for agent_id in mcp_tools.keys():
            logger.info(f"Loaded {len(mcp_tools[agent_id])} MCP tools for agent {agent_id}")
    except Exception as e:
        logger.exception("Failed to load MCP tools", exc_info=e)
        mcp_tools = []

    api_searcher_subagent = SubAgent(
        name="api-searcher",
        description="Собирает данные из различных API, обрабатывает результат, сохраняет результат в файл."
                    "Может использоваться и для обычного обращения к API. "
                    "Ты обязан использовать его, если пользователь просит собрать данные из API.",
        system_prompt="Ты субагент, который собирает данные из API.",
        tools=mcp_tools.get("api-searcher", []),
        skills=[(workspace_path.parent / "skills" / "research").as_posix()],
    )

    data_analyst_subagent = SubAgent(
        name="data-analyst",
        description="Анализирует данные, отвечает на вопросы на их основе. "
                    "Использовать, когда пользователь задает вопросы по уже собранным данным.",
        system_prompt="Ты субагент - аналитик данных. "
                      "Твоя задача - проанализировать поданные данные и максимально точно ответить на вопросы с опорой на данные.",
        skills=[(workspace_path.parent / "skills" / "analysis").as_posix()],
    )

    agent = create_deep_agent(
        name="main",
        model=model,
        checkpointer=MemorySaver(),
        backend=backend,
        tools=mcp_tools.get("main", []),
        subagents=[api_searcher_subagent, data_analyst_subagent],
        system_prompt=f"Текущая дата и время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
                      f"Твоя рабочая директория - {workspace_path.as_posix()}. Сохраняй файлы и работай там."
                      f"Прежде чем начинать выполнение задачи, ты обязан проверить, есть ли специализированные субагенты под эту задачу."
    )

    return agent


async def __get_mcp_tools() -> dict[str, list]:
    with open(Path(__file__).parent.parent / "mcp.json", encoding="utf-8") as f:
        config = json.load(f)

    result = {}
    async def __await_tools_and_save(_key: str, _client: MultiServerMCPClient):
        result[_key] = await _client.get_tools()

    tasks = []
    for agent_id in config.keys():
        mcp_client = MultiServerMCPClient(config[agent_id])
        tasks.append(__await_tools_and_save(agent_id, mcp_client))

    await asyncio.gather(*tasks, return_exceptions=True)

    return result
