import json
from pathlib import Path

HISTORY_FILE = Path(__file__).with_name("chat_history.json")

def load_chat_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []

def save_chat_history(user_message, ai_response):
    history = load_chat_history()
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": ai_response})
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)
    return history

def get_chat_history():
    loaded_history =  load_chat_history()
    return loaded_history







