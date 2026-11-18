from .chat_history import get_chat_history, save_chat_history

print(get_chat_history())

save_chat_history(
    "Hello",
    "Hello! How can I help you?"
)

save_chat_history(
    "What is Python?",
    "Python is a programming language."
)