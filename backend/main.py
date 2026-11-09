from fastapi import FastAPI
from backend.llm_service import (
    generate_questions as generate_ai_questions,
    generate_sample_answer
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AI Interview Preparation Assistant!"}


@app.get("/generate-questions")
def get_questions(role: str):

    questions = generate_ai_questions(role)

    return {
        "job_role": role,
        "questions": questions
    }


@app.get("/generate-answer")
def get_sample_answer(role: str, question: str):

    answer = generate_sample_answer(role, question)

    return {
        "job_role": role,
        "question": question,
        "sample_answer": answer
    }