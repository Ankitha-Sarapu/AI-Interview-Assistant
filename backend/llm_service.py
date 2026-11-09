
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_questions(role):

    prompt = f"""
    You are an experienced technical interviewer.

    Generate 5 interview questions for a fresher applying
    for the role of {role}.

    Include:
    1. Basic technical questions
    2. Conceptual questions
    3. Practical questions
    4. One HR question

    Keep the questions beginner-friendly.
    Return only the questions as a numbered list.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    questions = response.text.strip().split("\n")

    questions = [
        question.strip().lstrip("0123456789. ")
        for question in questions
        if question.strip()
    ]

    return questions
def generate_sample_answer(role, question):

    prompt = f"""
    You are an experienced interview coach.

    Generate a sample answer for a fresher applying
    for the role of {role}.

    Interview Question: {question}

    Instructions:
    1. Use simple and natural English.
    2. Keep the answer beginner-friendly.
    3. Explain the concept clearly.
    4. Include a practical example if needed.
    5. Keep the answer concise and interview-ready.

    Return only the sample answer.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text.strip() 