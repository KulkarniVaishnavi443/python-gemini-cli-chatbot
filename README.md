# Python Gemini CLI Chatbot

A simple AI-powered command-line chatbot built using Python and Google's Gemini API. The chatbot allows users to ask questions, receive AI-generated responses, and maintain conversation history using JSON file storage.

## Features

- Interactive command-line interface
- AI-generated responses using Google Gemini
- Conversation history management
- Persistent chat storage using JSON
- Environment variable management using `.env`
- Simple and modular Python project structure

## Tech Stack

- **Python**
- **Google Gen AI SDK**
- **Gemini API**
- **JSON**
- **python-dotenv**
- **uv** – Python project and dependency management

## Project Structure

```text
mini_project_python/
│
├── src/
│   └── mini_project_python/
│       ├── __init__.py
│       ├── main.py
│       ├── ai_service.py
│       ├── chat_history.py
│       └── chat_history.json  # Generated at runtime; not committed
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-gemini-cli-chatbot.git
```

### 2. Navigate to the project directory

```bash
cd python-gemini-cli-chatbot
```

### 3. Install dependencies

If you have uv installed:

```bash
uv sync
```

Alternatively, using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the chatbot

From the project root, execute:

```bash
uv run python -m mini_project_python.main
```

## How It Works

1. The user enters a question through the command-line interface.
2. The application retrieves previously stored conversation history.
3. The question and conversation context are passed to the Gemini API.
4. Gemini generates a response.
5. The response is displayed in the terminal.
6. The user message and AI response are saved in a JSON file.

## Learning Outcomes

Through this project, I explored:

- Python modular programming
- Working with external APIs
- Environment variable management
- JSON file handling
- Maintaining conversation context
- Basic AI chatbot development

## Future Improvements

- Add API error handling
- Build a FastAPI backend
- Develop a web-based chatbot interface

---

**Author:** Kulkarni Vaishnavi