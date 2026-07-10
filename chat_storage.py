from pathlib import Path
import json
from datetime import datetime


# Project directories
BASE_DIR = Path(__file__).parent
BIT_DIR = BASE_DIR / ".bit"
CHAT_DIR = BIT_DIR / "chats"

CHAT_DIR.mkdir(parents=True, exist_ok=True)


# Create a new chat file
def create_chat_file():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    chat_file = CHAT_DIR / f"{timestamp}.json"

    data = {
        "title": "Untitled Chat",
        "created_at": timestamp,
        "messages": []
    }

    with open(chat_file, "w") as f:
        json.dump(data, f, indent=4)

    return chat_file

# Save messages to disk
def save_messages(chat_file, messages):
    with open(chat_file, "w") as f:
        json.dump(messages, f, indent=4)


# Load a chat from disk
def load_chat(chat_file):
    with open(chat_file, "r") as f:
        return json.load(f)


# Get newest chat files first
def get_recent_chats(limit=10):
    chats = sorted(
        CHAT_DIR.glob("*.json"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    return chats[:limit]