# ❄ BIT — Binary Intelligence Tool

> A local-first AI assistant built with Python, Textual, Ollama, and a touch of Y2K nostalgia.

BIT (Binary Intelligence Tool) is a terminal-based AI assistant designed for developers, Linux enthusiasts, and builders who want a fast, private, and customizable AI experience.

Powered entirely by local models through Ollama, BIT runs on your own machine with no subscriptions, no API costs, and no cloud dependency.

---

## ✨ Features

### Current Features

* 🤖 Local AI using Ollama
* 💬 Chat interface built with Textual
* 🧠 Session memory
* 💾 Automatic chat logging
* 📜 Scrollable conversation history
* 🎨 Y2K / GenXSoftClub-inspired interface
* ⚡ Async responses (UI stays responsive)
* 🔒 Fully local and private

### Planned Features

* 📂 Open previous conversations
* 🔍 Search chat history
* 🏷 AI-generated chat titles
* 📁 Project awareness
* 📝 File editing
* 🌳 File explorer sidebar
* 🔧 Git integration
* 🤝 Aider integration
* 🎵 Optional music mode
* ✨ Advanced Y2K visual effects

---

## 📸 Philosophy

BIT is inspired by:

* Early 2000s internet culture
* Y2K Blue aesthetics
* GenXSoftClub design language
* Linux and open-source software
* Futuristic operating systems from the early web era

The goal is not to recreate ChatGPT.

The goal is to create a personal AI workstation that feels like a futuristic developer console from an alternate version of 2005.

---

## 🏗 Tech Stack

* Python
* Textual
* Rich
* Ollama
* Qwen 2.5 Coder
* JSON-based chat storage

---

## 🚀 Installation

### 1. Install Ollama

Follow the official installation instructions:

https://ollama.com

---

### 2. Pull a model

Example:

```bash
ollama pull qwen2.5-coder:7b
```

---

### 3. Clone the project

```bash
git clone <your-repository-url>
cd bit
```

---

### 4. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Fish shell:

```fish
source .venv/bin/activate.fish
```

---

### 5. Install dependencies

```bash
pip install textual rich requests
```

---

### 6. Start Ollama

```bash
ollama serve
```

---

### 7. Launch BIT

```bash
python main.py
```

---

## 📁 Project Structure

```text
bit/
├── main.py
├── bit_ai.py
├── chat_storage.py
├── README.md
└── .bit/
    └── chats/
```

---

## 🧠 Memory System

BIT stores conversation history during runtime using Ollama's chat API.

Example:

```text
You: My favorite distro is EndeavourOS.

You: What distro do I like?

BIT: Your favorite distro is EndeavourOS.
```

---

## 💾 Chat Logs

Every session automatically creates a chat log.

Example:

```text
~/.bit/chats/

2026-07-09_18-30-11.json
2026-07-09_19-02-45.json
2026-07-09_19-48-21.json
```

Logs are stored as JSON and can be loaded in future versions of BIT.

---

## 🎯 Vision

BIT is evolving toward a complete local AI development environment.

Future versions aim to provide:

* Persistent conversations
* Project-aware coding assistance
* Git integration
* Local code generation
* AI-powered workflows
* A fully customizable cyber-terminal experience

---

## License

MIT License

---

Built by developers who think terminals should have personality.
