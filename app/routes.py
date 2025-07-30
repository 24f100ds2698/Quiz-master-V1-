from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, login_user, logout_user, current_user
from app import db
from .models import User, Admin
from datetime import datetime
from app.models import Subject

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html') 


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash("Logged in successfully", "success")
            return redirect(url_for('user.dashboard'))
        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')

@main.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.query.filter_by(username=username, password=password).first()

        if admin:
            session['admin_logged_in'] = True
            session['admin_username'] = admin.username
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials.', 'danger')
            return redirect(url_for('main.admin_login'))

    return render_template('admin_login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        qualification = request.form.get('qualification')
        birth_date_str = request.form.get('birth_date')

        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()

        new_user = User(
            fullname=fullname,
            email=email,
            password=password,
            qualification=qualification,
            birth_date=birth_date
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for('main.login'))
