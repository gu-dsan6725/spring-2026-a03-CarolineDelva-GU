from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question: str, context: str):

    prompt = f"""
        You are analyzing a GitHub repository.

        Rules:
        1. Answer only using the provided context.
        2. Include file paths and line numbers.
        3. If unsure, say the context does not contain the answer.

        QUESTION:
        {question}

        CODEBASE CONTEXT:
        {context}

        ANSWER:
    """

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return completion.choices[0].message.content