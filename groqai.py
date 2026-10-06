from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from the .env file")

client = Groq(api_key=api_key)


def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful personal voice assistant. "
                        "Answer clearly and naturally. "
                        "Keep responses short because they will be spoken aloud."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        print("AI error:", error)
        return "Sorry sir, I am unable to connect to the AI right now."