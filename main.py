from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static
from rich.panel import Panel
from rich.text import Text

from bit_ai import (
    chat,
    generate_chat_title
)

from chat_storage import (
    create_chat_file,
    save_messages,
    load_chat,
    load_messages,
    get_recent_chats,
    get_chat_title,
    update_chat_title
)

import asyncio

SYSTEM_PROMPT = """
You are BIT.

BIT stands for Binary Intelligence Tool.

You are a futuristic AI assistant inspired by:
- Linux
- Open Source Software
- Y2K Technology
- Software Engineering

You help with:
- Programming
- Linux
- Web Development
- Design
- AI

Be concise, helpful and technically accurate.
"""


class IcyHeader(Static):
    def on_mount(self):
        logo = Text(
            """
 ██╗ ██████╗██╗   ██╗
 ██║██╔════╝╚██╗ ██╔╝
 ██║██║      ╚████╔╝
 ██║██║       ╚██╔╝
 ██║╚██████╗   ██║
 ╚═╝ ╚═════╝   ╚═╝
            """,
            style="#66ccff",
        )

        self.update(
            Panel(
                logo,
                title="❄ BIT",
                subtitle="Binary Intelligence Tool",
                border_style="#00ccff",
            )
        )


class Message(Static):
    pass


class BIT(App):
    CSS = """
    Screen {
        background: #020817;
        color: white;
    }

    #status {
        height: 3;
        border: round #00ccff;
        background: #041020;
        color: #99e6ff;
        padding: 0 1;
    }

    #chat {
        border: round #00ccff;
        background: #051425;
        padding: 1;
    }

    Input {
        border: round #33ccff;
        background: #041020;
        color: white;
    }

    .user {
        margin: 1 0;
        padding: 1;
        background: #0a1f35;
        color: white;
    }

    .assistant {
        margin: 1 0;
        padding: 1;
        background: #082b3a;
        color: #ccf5ff;
    }

    .thinking {
        color: #66ccff;
        margin: 1 0;
    }
    """

    # Initialize application state
    def __init__(self):
        super().__init__()

        self.startup_mode = True
        self.recent_chats = get_recent_chats()

        self.chat_file = None
        self.messages = []

    def compose(self) -> ComposeResult:
        yield IcyHeader()

        yield Static(
            "⚡ Model: Qwen 2.5 Coder | 🖥 Ollama Local | ❄ BIT",
            id="status",
        )

        yield VerticalScroll(id="chat")

        yield Input(
            placeholder="Ask BIT something..."
        )

    # Show startup menu
    async def on_mount(self):
        chat_container = self.query_one("#chat", VerticalScroll)

        menu = "❄ BIT\n\nRecent Chats\n\n"

        if self.recent_chats:
            for i, chat_file in enumerate(self.recent_chats, start=1):

                title = get_chat_title(chat_file)

                menu += f"{i}. {title}\n"
        else:
            menu += "No chats found.\n"

        menu += "\nN. New Chat"

        await chat_container.mount(
            Message(
                menu,
                classes="assistant"
            )
        )

    async def on_input_submitted(self, event: Input.Submitted):
        user_text = event.value.strip()

        if not user_text:
            return

        chat_container = self.query_one(
            "#chat",
            VerticalScroll
        )

        # Rename chat
        if user_text.startswith("/rename "):

            parts = user_text.split(maxsplit=2)

            # Startup menu rename:
            # /rename 2 New Title
            if self.startup_mode:

                if len(parts) < 3:
                    await chat_container.mount(
                        Message(
                            "❌ Usage: /rename <chat_number> <new_title>",
                            classes="assistant"
                        )
                    )
                    return

                try:
                    index = int(parts[1]) - 1

                    if not (0 <= index < len(self.recent_chats)):
                        raise ValueError

                    new_title = parts[2]

                    chat_file = self.recent_chats[index]

                    update_chat_title(
                        chat_file,
                        new_title
                    )

                    await self.refresh_startup_menu()

                except ValueError:
                    await chat_container.mount(
                        Message(
                            "❌ Invalid chat number",
                            classes="assistant"
                        )
                    )

                event.input.value = ""
                return

            # Loaded chat rename:
            # /rename My New Title
            else:

                new_title = user_text.replace(
                    "/rename ",
                    "",
                    1
                ).strip()

                if not new_title:
                    await chat_container.mount(
                        Message(
                            "❌ Title cannot be empty",
                            classes="assistant"
                        )
                    )

                    event.input.value = ""
                    return  

                update_chat_title(
                    self.chat_file,
                    new_title
                )

                await chat_container.mount(
                    Message(
                        f"✏️ Chat renamed to:\n\n{new_title}",
                        classes="assistant"
                    )
                )

                event.input.value = ""
                return

        # Startup menu handling
        if self.startup_mode:

            selection = user_text.lower()

            # Create new chat
            if selection == "n":

                self.chat_file = create_chat_file()

                self.messages = [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    }
                ]

                save_messages(
                    self.chat_file,
                    self.messages
                )

                self.startup_mode = False

                await chat_container.mount(
                    Message(
                        f"🚀 New Chat\n\n{self.chat_file.name}",
                        classes="assistant"
                    )
                )

                chat_container.scroll_end()

                return

            # Load old chat
            if selection.isdigit():

                index = int(selection) - 1

                if 0 <= index < len(self.recent_chats):

                    self.chat_file = self.recent_chats[index]

                    self.messages = load_messages(
                        self.chat_file
                    )

                    self.startup_mode = False

                    await chat_container.mount(
                        Message(
                            f"📂 Loaded Chat\n\n{self.chat_file.name}",
                            classes="assistant"
                        )
                    )

                    # Render previous chats
                    for message in self.messages:

                        # Never show the system prompt
                        if message["role"] == "system":
                            continue

                        if message["role"] == "user":
                            await chat_container.mount(
                                Message(
                                    f"👤 {message['content']}",
                                    classes="user"
                                )
                            )

                        elif message["role"] == "assistant":
                            await chat_container.mount(
                                Message(
                                    f"🤖 BIT\n\n{message['content']}",
                                    classes="assistant"
                                )
                            )

                    chat_container.scroll_end()

                    return
 
            await chat_container.mount(
                Message(
                    "❌ Invalid selection",
                    classes="assistant"
                )
            )

            return

        # Normal chat mode
        await chat_container.mount(
            Message(
                f"👤 {user_text}",
                classes="user"
            )
        )

        thinking = Message(
            "⚡ Thinking...",
            classes="thinking"
        )

        await chat_container.mount(thinking)

        # First user message Becomes chat title
        if len(self.messages) == 1:

            try:
                title = await asyncio.to_thread(
                    generate_chat_title,
                    user_text
                )

                update_chat_title(
                    self.chat_file,
                    title
                )

            except Exception:
                pass

        self.messages.append(
            {
                "role": "user",
                "content": user_text
            }
        )

        save_messages(
            self.chat_file,
            self.messages
        )

        try:
            reply = await asyncio.to_thread(
                chat,
                self.messages
            )

            self.messages.append(
                {
                    "role": "assistant",
                    "content": reply
                }
            )

            save_messages(
                self.chat_file,
                self.messages
            )

        except Exception as e:
            reply = f"❌ Error:\n{e}"

        thinking.remove()

        await chat_container.mount(
            Message(
                f"🤖 BIT\n\n{reply}",
                classes="assistant"
            )
        )

        chat_container.scroll_end()

    # Rebuild startup menu
    async def refresh_startup_menu(self):
        chat_container = self.query_one(
            "#chat",
            VerticalScroll
        )

        # Clear existing widgets
        await chat_container.remove_children()

        self.recent_chats = get_recent_chats()

        menu = "❄ BIT\n\nRecent Chats\n\n"

        if self.recent_chats:
            for i, chat_file in enumerate(
                self.recent_chats,
                start=1
            ):
                title = get_chat_title(chat_file)

                menu += f"{i}. {title}\n"
        else:
            menu += "No chats found.\n"

        menu += "\nN. New Chat"

        await chat_container.mount(
            Message(
                menu,
                classes="assistant"
            )
        )

    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
    ]


if __name__ == "__main__":
    BIT().run()