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
    data = load_chat(chat_file)

    data["messages"] = messages

    with open(chat_file, "w") as f:
        json.dump(data, f, indent=4)


# Load a chat from disk
def load_chat(chat_file):
    with open(chat_file, "r") as f:
        return json.load(f)


# Get only the messages from a chat
def load_messages(chat_file):
    data = load_chat(chat_file)

    # Old format
    if isinstance(data, list):
        return data

    return data["messages"]
    
# Get chat title
def get_chat_title(chat_file):
    data = load_chat(chat_file)

    #Old chat format
    if isinstance(data, list):
        return chat_file.stem

    return data["title"]

# Get newest chat files first
def get_recent_chats(limit=10):
    chats = sorted(
        CHAT_DIR.glob("*.json"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    return chats[:limit]

# Update chat title
def update_chat_title(chat_file, title):
    data = load_chat(chat_file)

    # Skip legacy chats
    if isinstance(data, list):
        return

    data["title"] = title

    with open(chat_file, "w") as f:
        json.dump(data, f, indent=4)