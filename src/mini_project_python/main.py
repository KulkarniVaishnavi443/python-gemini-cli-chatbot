from .ai_service import generate_answer
from .chat_history import get_chat_history, save_chat_history


def display_welcome():
    print("""===================================
                    AI Q&A ASSISTANT
             =================================== """ )
    print("Hello! Welcome to your AI assistant.")
    print("What would you like to ask?")

def get_user_input():
    user_input = input("\nYou: ")
    return user_input

def run_application():
    history = get_chat_history()
    display_welcome()
    while True:
        user_input = get_user_input()
        if user_input.strip().lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        elif user_input.strip() == "":
            print("Please enter a valid input.")
            continue
        else:
            answer = generate_answer(user_input, history)
            print(f"\nAssistant: {answer}\n")
            save_chat_history(user_input, answer)
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    run_application()


