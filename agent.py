import requests
from tools import TOOLS, handle_tool_call

def chat(user_message, history):
    history.append({"role": "user", "content": user_message})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen2.5:3b",
            "messages": history,
            "tools": TOOLS,
            "stream": False
        }
    )

    data = response.json()
    message = data["message"]
    if message.get("tool_calls"):
        tool_name = message["tool_calls"][0]["function"]["name"]
        tool_args = message["tool_calls"][0]["function"]["arguments"]
        return handle_tool_call(tool_name, tool_args)
    return message["content"]
