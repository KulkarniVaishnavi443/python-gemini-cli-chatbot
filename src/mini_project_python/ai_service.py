from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def generate_answer(question, history):
    conversation = ""

    for message in history:
        role = message["role"]
        content = message["content"]

        if role in ["ai", "assistant"]:
            role = "Assistant"
        else:
            role = "User"

        conversation += f"{role}: {content}\n"

    conversation += f"User: {question}"
    response = client.interactions.create(
        model = "gemini-3.5-flash-lite",
        input = conversation
    )

    return response.output_text





