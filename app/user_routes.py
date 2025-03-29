from flask import Blueprint, rende_template
from flask_login import login_required

user=Blueprint('user',__name__)

@user.route('/dashborad')
@login_required
def dashboard():
  return render_template('user_dashboard.html')
