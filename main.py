from database import init_db
from agent import chat

init_db()
history = []
print("Welcome to the chat! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = chat(user_input, history)
    print("Agent:", reply)