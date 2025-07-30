from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(200))
    birth_date = db.Column(db.Date)
    
    scores = db.relationship('Score', backref='user', lazy=True)  


class Admin(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    
    chapters = db.relationship('Chapter', backref='subject', lazy=True)


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    
    quizzes = db.relationship('Quiz', backref='chapter', lazy=True)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    date = db.Column(db.Date)
    duration = db.Column(db.String(10))  
    
    questions = db.relationship('Question', backref='quiz', lazy=True)
    scores = db.relationship('Score', backref='quiz', lazy=True)  # ✅ helpful for admin too


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500))
    option_a = db.Column(db.String(100))
    option_b = db.Column(db.String(100))
    option_c = db.Column(db.String(100))
    option_d = db.Column(db.String(100))
    correct_answer = db.Column(db.String(1))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))



class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    
    score = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

