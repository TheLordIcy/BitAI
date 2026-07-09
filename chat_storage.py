from pathlib import Path
import json
from datetime import datetime

BIT_DIR = Path.home()/ ".bit"
CHAT_DIR =BIT_DIR / "chats"

CHAT_DIR.mkdir(parents=True, exist_ok=True)



def create_chat_file():
    timestamp = datetime.now(). strftime("%Y-%m-%d_%H-%M-%S")
    chat_file = CHAT_DIR / f"{timestamp}.json"

    with open(chat_file, "w") as f:
        json.dump([], f)

    return chat_file

def save_messages(chat_file, messages):
    with open(chat_file, "w") as f:
        json.dump(messages, f, indent=4)    