# ❄ BIT

**Binary Intelligence Tool**

A futuristic terminal-based AI assistant powered by **Ollama**, **Qwen 2.5 Coder**, and **Textual**.

BIT is inspired by Linux, open-source software, Y2K technology, and software engineering workflows. It runs entirely on your machine and provides a clean terminal interface for chatting with local AI models.

---

## Features

* 💬 Persistent chat history
* 📂 Load previous conversations
* 🏷️ AI-generated chat titles
* ✏️ Rename chats
* 🗑️ Delete chats
* ⚡ Streaming responses
* 💻 Coding Mode
* 🤖 Assistant Mode
* 🏠 Startup menu with recent chats
* 🔒 Fully local using Ollama
* 🎨 Y2K-inspired terminal UI

---

## Tech Stack

* Python
* Textual
* Ollama
* Qwen 2.5 Coder
* Rich

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/bit.git
cd bit
```

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama:

https://ollama.com

Pull the default model:

```bash
ollama pull qwen2.5-coder:7b
```

### Run BIT

```bash
python main.py
```

---

## Commands

| Command            | Description             |
| ------------------ | ----------------------- |
| `/help`            | Show available commands |
| `/home`            | Return to startup menu  |
| `/new`             | Create a new chat       |
| `/rename <title>`  | Rename current chat     |
| `/delete <number>` | Delete a chat           |
| `/code`            | Enable coding mode      |
| `/normal`          | Enable assistant mode   |

---

## Screenshots



---

## Project Structure

```text
bit/
├── main.py
├── bit_ai.py
├── chat_storage.py
├── requirements.txt
└── .bit/
    └── chats/
```

---

## Roadmap

### v1.1

* Improved header/logo
* Chat search
* Export conversations
* Better startup menu
* Theme customization
* Improved code rendering

---

## License

MIT License

---

Built with ❄ by Icy.
