# Backend LLM

## Setup

Install Python

Install UV and install all packages with `uv sync`. Also install a virtual environment with `uv venv`.

Install Ollama and _gemma3:4b_ or _llama3.2_ or _deepseek-r1_ and set the used model in the file llm.py.

To run the application in development mode, use the following command:

```bash
uv run fastapi dev
```

To run the application in production mode, use the following command:

```bash
fastapi run
```

Interactive API docs: go to http://127.0.0.1:8000/docs

Ask a question: http://127.0.0.1:8000/fun-fact?category=CATEGORY
