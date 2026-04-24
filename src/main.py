import asyncio
from acp import run_agent
from deepagents_acp.server import AgentServerACP
import dotenv
from loguru import logger

from src.agent import create_agent


async def main():
    dotenv.load_dotenv()

    agent = await create_agent()

    server = AgentServerACP(agent)

    logger.info("Starting server...")
    await run_agent(server)


if __name__ == '__main__':
    asyncio.run(main())