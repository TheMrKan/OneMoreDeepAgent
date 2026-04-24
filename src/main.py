import asyncio
from acp import run_agent
from deepagents_acp.server import AgentServerACP
import dotenv

from src.agent import create_agent


async def main():
    dotenv.load_dotenv()

    agent = create_agent()

    server = AgentServerACP(agent)

    await run_agent(server)


if __name__ == '__main__':
    asyncio.run(main())