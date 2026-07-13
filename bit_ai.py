import json
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

def generate_chat_title(first_message):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": f"""
Generate a short chat title.

Rules:
- 2 to 5 words
- No quotes
- No punctuation
- Professional
- Summarize the user's request

User message:
{first_message}

Title:
""",
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()

    return (
        response.json()["response"]
        .strip()
        .replace('"', '')
        .replace("'", "")
        
        )

# Stream response from Ollama
def stream_chat(messages):

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": True
        },
        stream=True,
        timeout=300
    )

    response.raise_for_status()

    for line in response.iter_lines():

        if not line:
            continue

        data = json.loads(line)

        if "message" in data:
            yield data["message"]["content"]