from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InterviewLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300))
    answer = db.Column(db.String(500))
    score = db.Column(db.Integer)
    feedback = db.Column(db.String(500))