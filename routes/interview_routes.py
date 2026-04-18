from flask import Blueprint, request, jsonify
from models.interview import db, InterviewLog

interview_bp = Blueprint("interview_bp", __name__)

# ==============================
# QUESTION BANK
# ==============================
QUESTION_BANK = {
    "os": [
        "What is a deadlock?",
        "Explain paging vs segmentation",
        "What is a process vs thread?"
    ],
    "db": [
        "What is normalization?",
        "Explain indexing",
        "What is ACID?"
    ],
    "ds": [
        "What is a stack vs queue?",
        "Explain time complexity",
        "What is a hash table?"
    ]
}

# ==============================
# GENERATE QUESTIONS
# ==============================
@interview_bp.route("/generate-questions", methods=["POST"])
def generate_questions():
    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Topic is required"}), 400

    topic = data["topic"].lower()

    if topic in QUESTION_BANK:
        return jsonify({"questions": QUESTION_BANK[topic]})
    else:
        return jsonify({"questions": ["Topic not found. Use os, db, or ds"]})


# ==============================
# EVALUATE ANSWER
# ==============================
@interview_bp.route("/evaluate-answer", methods=["POST"])
def evaluate_answer():
    data = request.get_json()

    if not data or "question" not in data or "answer" not in data:
        return jsonify({"error": "Question and answer required"}), 400

    question = data["question"]
    answer = data["answer"].lower()

    # Simple scoring logic
    score = 5
    feedback = "Basic answer"

    if len(answer) > 20:
        score = 7
        feedback = "Good explanation"

    if "deadlock" in answer or "process" in answer:
        score = 9
        feedback = "Strong technical answer"

    # Save to database
    log = InterviewLog(
        question=question,
        answer=answer,
        score=score,
        feedback=feedback
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({
        "score": score,
        "feedback": feedback
    })


# ==============================
# GET HISTORY (IMPORTANT FIX)
# ==============================
@interview_bp.route("/history", methods=["GET"])
def get_history():
    logs = InterviewLog.query.all()

    return jsonify([
        {
            "question": log.question,
            "answer": log.answer,
            "score": log.score,
            "feedback": log.feedback
        } for log in logs
    ])