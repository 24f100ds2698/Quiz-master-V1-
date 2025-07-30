from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from .models import Quiz, Question, Score
from app import db
from datetime import datetime

quiz = Blueprint('quiz', __name__)

@quiz.route('/start')
@login_required
def start_quiz():
    quizzes = Quiz.query.all()
    return render_template('quiz.html', quizzes=quizzes)

@quiz.route('/<int:quiz_id>/start')
@login_required
def begin_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    session['quiz_id'] = quiz_id
    session['current_question_index'] = 0
    session['answers'] = {}
    return redirect(url_for('quiz.question', quiz_id=quiz_id, index=0))

@quiz.route('/<int:quiz_id>/question/<int:index>', methods=['GET', 'POST'])
@login_required
def question(quiz_id, index):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions
    total = len(questions)

    if request.method == 'POST':
        selected = request.form.get('option')
        if selected is not None:
            session['answers'][str(questions[index - 1].id)] = selected

        if 'next' in request.form and index < total:
            return redirect(url_for('quiz.question', quiz_id=quiz_id, index=index))
        elif 'prev' in request.form and index > 1:
            return redirect(url_for('quiz.question', quiz_id=quiz_id, index=index - 2))
        elif 'submit' in request.form:
            return redirect(url_for('quiz.submit_quiz', quiz_id=quiz_id))

    if index >= total:
        return redirect(url_for('quiz.submit_quiz', quiz_id=quiz_id))

    question = questions[index]
    selected_answer = session['answers'].get(str(question.id), None)

    return render_template('take_quiz.html', quiz=quiz, question=question, index=index + 1, total=total, selected=selected_answer)

@quiz.route('/submit/<int:quiz_id>')
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    answers = session.get('answers', {})
    score = 0

    for question in quiz.questions:
        qid = str(question.id)
        if qid in answers and answers[qid] == question.correct_answer:
            score += 1

    new_score = Score(user_id=current_user.id, quiz_id=quiz.id, score=score, timestamp=datetime.now())
    db.session.add(new_score)
    db.session.commit()

    session.pop('answers', None)
    session.pop('quiz_id', None)
    session.pop('current_question_index', None)

    return render_template('score_result.html', score=score, total=len(quiz.questions))




