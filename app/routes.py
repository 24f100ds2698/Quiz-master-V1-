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

@main.route('/login')
def login():
    return render_template('login.html')  

@main.route('/dashboard')
@login_required  
def dashboard():
    return render_template('dashboard.html', user=current_user)
