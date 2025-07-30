from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from .models import Subject, Chapter, Quiz, Question, Score
from datetime import datetime

user = Blueprint('user', __name__)

@user.route('/dashboard')
@login_required
def dashboard():
    subjects = Subject.query.all()
    return render_template('user_dashboard.html', subjects=subjects)

@user.route('/chapters/<int:subject_id>')
@login_required
def chapters(subject_id):
    chapters = Chapter.query.filter_by(subject_id=subject_id).all()
    return render_template('chapters.html', chapters=chapters, subject_id=subject_id)

@user.route('/quizzes/<int:chapter_id>')
@login_required
def quizzes(chapter_id):
    quizzes = Quiz.query.filter_by(chapter_id=chapter_id).all()
    return render_template('quizzes.html', quizzes=quizzes, chapter_id=chapter_id)

@user.route('/quiz/<int:quiz_id>', methods=['GET'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions
    return render_template('take_quiz.html', quiz=quiz, questions=questions)


@user.route('/score/<int:quiz_id>')
@login_required
def view_score(quiz_id):
    score = Score.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).first()
    quiz = Quiz.query.get_or_404(quiz_id)
    total = len(quiz.questions)
    
    return render_template("score_result.html", score=score.score, total=total)

@user.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions
    score = 0

    for q in questions:
        selected = request.form.get(f'q{q.id}')
        if selected == q.correct_answer:
            score += 1

    new_score = Score(user_id=current_user.id, quiz_id=quiz.id,
                      score=score, timestamp=datetime.now())
    db.session.add(new_score)
    db.session.commit()

    return redirect(url_for('user.view_score', quiz_id=quiz.id))

