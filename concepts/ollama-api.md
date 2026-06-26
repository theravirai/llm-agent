# Ollama API

1. The model's reply comes back in the `response` field of the JSON.

2. `ollama pull` downloads the model to your machine.
   `ollama run` starts the model so you can chat with it.

3. `localhost` means "this same machine". Port `11434` is where Ollama
   listens for requests. So `http://localhost:11434` means we are sending
   requests to a program running locally, not over the internet.