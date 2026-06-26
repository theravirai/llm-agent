from database import get_username, save_username



# This structure is a schema (or format) that tells the LLM:
# "These are the tools you are allowed to use, and this is how you should call them."
# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "save_username",
#             "description": "Save the user's name to the database",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "username": {
#                         "type": "string",
#                         "description": "The name to save"
#                     }
#                 },
#                 "required": ["username"]
#             }
#         }
#     }
# ]



TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "save_username",
            "description": "Save the user's name to the database",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string",
                        "description": "The name to save"
                    }
                },
                "required": ["username"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_username",
            "description": "Retrieve the user's name from the database",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

def handle_tool_call(tool_name, tool_args):
    if tool_name == "save_username":
        save_username(tool_args["username"])
        return f"Saved username: {tool_args['username']}"

    elif tool_name == "get_username":
        return get_username()

    return "Unknown tool"