from . import db
from flask_login import UserMixin

class Participant(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(75), unique=True, nullable=False)
    passkey = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(200))  
    birth_date = db.Column(db.Date)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    passkey = db.Column(db.String(50), nullable=False) 

class SubjectMatter(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text)

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject_matter.id'), nullable=False)
    topic = db.Column(db.String(250), nullable=False)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    scheduled_on = db.Column(db.Date) 
    duration = db.Column(db.String(10))

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    problem_text = db.Column(db.Text, nullable=False)
    option_1 = db.Column(db.String(250))
    option_2 = db.Column(db.String(250))
    option_3 = db.Column(db.String(250))
    option_4 = db.Column(db.String(250))
    correct_answer = db.Column(db.Integer)

class ScoreCard(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)  
    marks_obtained = db.Column(db.Integer) 
