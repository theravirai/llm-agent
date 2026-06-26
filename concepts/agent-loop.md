# Agent Loop

1. We maintain a `history` list and pass it into the `chat()` function on 
   every call. This is necessary because the model has no memory between 
   requests. Each time we call `chat()`, the model only knows what we send 
   it in that moment. By passing the history (stored in database), the model can see the saved name.

   To be precise, when a user provides their name, we save it to a database. 
   This means the data survives even if the program restarts, the model 
   can retrieve it in a future session.

2. Ollama runs as a separate server process. It loads the AI model into 
   memory and listens for requests at `http://localhost:11434`. Our Python 
   program is a client, it sends HTTP POST requests to Ollama and reads 
   the response. The two are separate programs communicating over HTTP.

3. When the model decides to call a tool instead of replying with text, it 
   returns a structured JSON response containing `tool_calls`. Our code 
   detects this, extracts the tool name and arguments, and calls the 
   matching Python function. The result is then added back to the history 
   so the model knows what happened.