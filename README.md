# AI Interview Preparation Assistant

An AI-powered application that helps freshers prepare for technical interviews by generating interview questions and sample answers based on their chosen job role.

## Features

- Generate interview questions dynamically using Google Gemini.
- Generate AI-powered sample answers for individual questions.
- Display questions in expandable sections.
- Download interview questions and sample answers as a text file.
- Simple and user-friendly interface.
- Backend connection and error handling.

## Technologies Used

- Python
- FastAPI
- Streamlit
- Large Language Models (LLMs)
- Google Gemini API
- Prompt Engineering
- Requests
- Python-dotenv

## Project Structure

```text
AI-Interview-Assistant/
│
├── backend/
│   ├── main.py
│   └── llm_service.py
│
├── frontend/
│   └── app.py
│
├── .env (create locally)
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ankitha-Sarapu/AI-Interview-Assistant.git
```

### 2. Navigate to the project folder

```bash
cd AI-Interview-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install fastapi uvicorn streamlit requests python-dotenv google-genai
```

### 6. Configure the Gemini API key

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

## Running the Application

### 1. Start the FastAPI backend

Open the first terminal and run:

```bash
uvicorn backend.main:app --reload
```

Backend URL:

http://127.0.0.1:8000

### 2. Start the Streamlit frontend

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run frontend/app.py
```

Frontend URL:

http://localhost:8501

## How to Use

1. Open the application in your browser.
2. Enter a job role, such as Python Developer.
3. Click Generate Interview Questions.
4. Expand a question to view it.
5. Click Generate Sample Answer to get an AI-generated answer.
6. Download your interview questions and answers for future preparation.

## Future Improvements

- Add more interview categories.
- Support additional programming languages.
- Improve answer personalization.

## Author

Ankitha Sarapu
