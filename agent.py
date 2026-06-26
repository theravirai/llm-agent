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
        
        # append assistant's tool call to history
        history.append(message)
        
        # execute the tool
        result = handle_tool_call(tool_name, tool_args)
        
        # append tool result to history
        history.append({"role": "tool", "content": str(result)})
        
        return result
    return message["content"]
