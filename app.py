from flask import Flask
from models.interview import db
from routes.interview_routes import interview_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interview.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(interview_bp)

@app.route("/")
def home():
    return {"message": "Interview Intelligence API running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)