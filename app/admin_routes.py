from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from .models import Subject, Chapter, Quiz, Question, Admin
from datetime import datetime

admin = Blueprint('admin', __name__)

@admin.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('admin_login.html')
    return render_template('admin_login.html')


@admin.route('/dashboard')
def dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))

    subjects = Subject.query.all()
    return render_template('admin_dashboard.html', subjects=subjects)


@admin.route('/add-subject', methods=['GET', 'POST'])
def add_subject():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))

    if request.method == 'POST':
        name = request.form.get('name')
        desc = request.form.get('description')
        subject = Subject(name=name, description=desc)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    return render_template('add_subject.html')

@admin.route('/add-chapter/<int:subject_id>', methods=['GET', 'POST'])
def add_chapter(subject_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))

    if request.method == 'POST':
        name = request.form.get('name')
        desc = request.form.get('description')
        chapter = Chapter(name=name, description=desc, subject_id=subject_id)
        db.session.add(chapter)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    return render_template('add_chapter.html', subject_id=subject_id)

@admin.route('/add-quiz/<int:chapter_id>', methods=['GET', 'POST'])
def add_quiz(chapter_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))

    if request.method == 'POST':
        date_str = request.form.get('date')  # This is a string like "2025-09-30"
        duration = request.form.get('duration')

        
        quiz_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        quiz = Quiz(chapter_id=chapter_id, date=quiz_date, duration=duration)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))

    return render_template('add_quiz.html', chapter_id=chapter_id)


@admin.route('/add-question/<int:quiz_id>', methods=['GET', 'POST'])
def add_question(quiz_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))

    if request.method == 'POST':
        text = request.form.get('text')
        a = request.form.get('option_a')
        b = request.form.get('option_b')
        c = request.form.get('option_c')
        d = request.form.get('option_d')
        correct = request.form.get('correct_answer')

        question = Question(
            quiz_id=quiz_id,
            question_text=text,
            option_a=a,
            option_b=b,
            option_c=c,
            option_d=d,
            correct_answer=correct
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    return render_template('add_question.html', quiz_id=quiz_id)


@admin.route('/admin_logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('admin.admin_login'))
