import requests


# Current Ollama model
MODEL = "qwen2.5-coder:7b"


# Send conversation to Ollama
def chat(messages):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    return response.json()["message"]["content"]