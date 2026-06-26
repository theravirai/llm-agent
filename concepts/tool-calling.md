# Tool Calling

1. The model cannot run Python code directly. It only outputs text.
   We give it a tool definition so it knows what tools exist, what they
   do, and what arguments they take. It then outputs a structured JSON
   block saying which tool to call and with what arguments.

2. `handle_tool_call` receives the tool name and arguments from the
   model's response and routes them to the correct Python function.
   It is the bridge between what the model wants to do and what
   actually runs on the machine.

3. `tool_args` is a dictionary like `{"username": "Alice"}`.
   We use `tool_args["username"]` to extract just the value we need,
   not pass the whole dictionary to the function.