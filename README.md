Interview Intelligence API

A RESTful backend API that simulates technical interviews by generating questions and evaluating candidate responses using scoring logic. Built with Flask and deployed on Render.

Live Demo

https://interview-intelligence-api-lxv6.onrender.com

Browser Test

https://interview-intelligence-api-lxv6.onrender.com/evaluate-browser?question=test&answer=hello

Features

- Generate interview questions by topic (Operating Systems, Databases, Data Structures)
- Evaluate answers with scoring logic
- Provide feedback on responses
- Store previous attempts in a database
- Browser-friendly testing endpoint

Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- Render (Deployment)

API Endpoints

Generate Questions

POST /generate-questions

Request Body:
{
  "topic": "os"
}

Response:
{
  "questions": [
    "What is a deadlock?",
    "Explain paging vs segmentation",
    "What is a process vs thread?"
  ]
}

Evaluate Answer

POST /evaluate-answer

Request Body:
{
  "question": "What is a deadlock?",
  "answer": "Deadlock occurs when processes wait indefinitely for resources."
}

Response:
{
  "score": 9,
  "feedback": "Strong technical answer"
}

Get History

GET /history

Response:
[
  {
    "question": "...",
    "answer": "...",
    "score": 8,
    "feedback": "..."
  }
]

Browser Test Endpoint

GET /evaluate-browser

Example:
/evaluate-browser?question=deadlock&answer=test

How to Run Locally

git clone https://github.com/pujithabandla/interview-intelligence-api.git
cd interview-intelligence-api
python -m venv venv
venv\Scripts\activate
pip install flask flask_sqlalchemy
python app.py

Project Overview

This project simulates technical interviews by generating domain-specific questions and evaluating responses using rule-based scoring. It also stores responses for tracking performance over time.

Future Improvements

- AI-powered evaluation using large language models
- Difficulty levels (easy, medium, hard)
- User authentication system
- Frontend interface for interactive use
- Advanced scoring using keyword analysis

Author

Pujitha Bandla

Why This Project

This project demonstrates backend API development, RESTful design, database integration, deployment, and real-world problem solving.

HOW TO USE IT
Go to your GitHub repo
Open README.md
Click Edit
Replace everything with this
Click Commit
