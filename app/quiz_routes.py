from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Quiz, Question, UserResponse
from . import db

quiz = Blueprint('quiz', __name__)

@quiz.route('/start')
@login_required  
def start_quiz():
    quizzes = Quiz.query.all()  
    return render_template('quiz.html', quizzes=quizzes)

@quiz.route('/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)  
    return render_template('take_quiz.html', quiz=quiz)

@quiz.route('/submit/<int:quiz_id>', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    score = 0

    for question in quiz.questions:
        user_answer = request.form.get(f'question-{question.id}')
        if user_answer and user_answer == question.correct_answer:
            score += 1

        
        response = UserResponse(
            user_id=current_user.id,
            question_id=question.id,
            selected_answer=user_answer,
            is_correct=(user_answer == question.correct_answer)
        )
        db.session.add(response)

    db.session.commit()
    flash(f'Quiz submitted! Your score: {score}/{len(quiz.questions)}', 'success')
    return redirect(url_for('user.dashboard'))  



