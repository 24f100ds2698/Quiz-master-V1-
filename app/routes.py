from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')  

@main.route('/about')
def about():
    return render_template('about.html') 

@main.route('/quiz/start')
@login_required 
def start_quiz():
    return render_template('quiz.html') 

from flask import request, redirect, url_for, flash
from flask_login import login_user
from .models import User  # or Participant/Admin depending on your logic

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(username=email_or_username).first()
        if user and user.password == password:  # NOTE: Add hashing later
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for('user.dashboard'))  # or admin.dashboard
        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')


@main.route('/dashboard')
@login_required  
def dashboard():
    return render_template('dashboard.html', user=current_user)
