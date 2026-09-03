import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from the .env file")

client = genai.Client(api_key=api_key)


def ask_ai(question):
    try:
        prompt = f"""
        You are Jarvis, a helpful personal voice assistant.
        Answer clearly in a natural conversational style.
        Keep the answer short, preferably under three sentences,
        because your response will be spoken aloud.

        User's question: {question}
        """

        response = client.interactions.create(
            model="gemini-3-flash-preview",
            input=prompt
        )

        return response.output_text

    except Exception as error:
        print("AI error:", error)
        return "Sorry sir, I am unable to connect to the AI right now."