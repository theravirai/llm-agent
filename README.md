# LLM Agent with Tool Calling using Ollama and SQLite

A terminal-based AI agent that runs locally using Ollama and SQLite.
The agent can save and retrieve a username through tool calls. The model decides when to call a tool, it is not hardcoded logic.

---

## How it works

The user types a message in the terminal. The message is sent to a local LLM running via Ollama. If the model decides it needs to save or retrieve
a name, it returns a tool call instead of a text reply. The Python code
detects this, runs the appropriate database function, and returns the result.

The full conversation history is passed to the model on every request
because the model has no memory between calls.

---

## Project structure

```
llm-agent/
├── main.py          # entry point, terminal chat loop
├── agent.py         # sends messages to Ollama, handles tool calls
├── tools.py         # tool definitions and dispatcher
├── database.py      # SQLite functions: init, save, get
├── concepts/        # notes written during development
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.13
- Ollama installed and running
- Model: qwen2.5:3b

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the model:

```bash
ollama pull qwen2.5:3b
```

---

## Running the Application

Start the Ollama server:

```bash
ollama serve
```

Open another terminal.

### macOS / Linux

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the application:

```bash
python3 main.py
```

### Windows (Command Prompt)

Activate the virtual environment:

```cmd
venv\Scripts\activate
```

Run the application:

```cmd
python main.py
```

---

## Example session

```
You: My name is Peter
Agent: Saved username: Peter

You: What is my username?
Agent: Your username is Peter.
```

---

## Model used

qwen2.5:3b via Ollama. Chosen because it is small enough to run on a local machine without a GPU and supports tool calling.

---

## Tool call parsing

When the model wants to call a tool, it returns a JSON response with a
`tool_calls` field instead of plain text. The code reads
`message["tool_calls"][0]["function"]["name"]` for the tool name and
`["arguments"]` for the parameters. It then dispatches to the matching
Python function in `database.py` and appends the result back to the
conversation history.

---
