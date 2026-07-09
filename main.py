from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static
from rich.panel import Panel
from rich.text import Text
from bit_ai import chat
import asyncio


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
    }
    """

    def __init__(self):
        super().__init__()

        self.messages = [
            {
                "role": "system",
                "content": """
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
            }
        ]

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

    async def on_mount(self):
        chat_container = self.query_one("#chat", VerticalScroll)

        await chat_container.mount(
            Message(
                "❄ Welcome to BIT\n\n🚀 Binary Intelligence Tool Online",
                classes="assistant"
            )
        )

    async def on_input_submitted(self, event: Input.Submitted):
        user_text = event.value.strip()

        if not user_text:
            return

        event.input.value = ""

        chat_container = self.query_one("#chat", VerticalScroll)

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

        self.messages.append(
            {
                "role": "user",
                "content": user_text
            }
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

    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
    ]


if __name__ == "__main__":
    BIT().run()