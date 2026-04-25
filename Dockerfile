FROM python:3.14-slim

RUN pip install uv
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync

RUN apt update
RUN apt install curl -y

COPY . .

CMD ["uv", "run", "-m", "src.main"]