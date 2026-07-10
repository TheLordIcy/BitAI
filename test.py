from chat_storage import get_recent_chats, load_chat

chats = get_recent_chats()

for i, chat in enumerate(chats, start=1):
    print(f"{i}. {chat.name}")

if chats:
    messages = load_chat(chats[0])

    print("\nLoaded chat:\n")

    for msg in messages:
        print(msg["role"], ":", msg["content"][:50])