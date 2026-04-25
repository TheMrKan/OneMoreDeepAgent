## Track: A+C

# Прототип агента на Deep Agents

## Специализация: 
- ### Поиск открытых API
- ### Сбор данных из API
- ### Анализ данных
- ### Визуализация
<br>

**Благодаря ACP интерфейсу совместим с большинством IDE и некоторыми CLI утилитами.**

## Технологии
- Фреймворк **Deep Agents** (LangChain + LangGraph)
- Связь с клиентом: **Agent Client Protocol** (ACP), транспорт: **stdio**. 
- **MCP** для поиска и исследования открытых API
- Основной многофункциональный агент с возможностью запуска 
узкоспециализированных **субагентов** (**api-searcher**, **data-analyst**)
- Доступ к файловой системе через инструменты **read_file**, **write_file** и т. д. (**FileSystemBackend**)
- Выполнение **Shell** команд (**LocalShellBackend**)
- Персональные **Skills** для каждого агента

## Skills
Добавляются в директорию `./skills` отдельно для каждого агента.<br>
Должны соответствовать стандарту: https://agentskills.io/specification

## MCP
MCP сервера добавляются в `./mcp.json` отдельно для каждого агента.

## Запуск
```bash
uv run -m src.main
```

Пример команды запуска в WSL для ACP клиента VS Code:
```bash
wsl --cd /home/user/agent/ uv run -m src.main
```