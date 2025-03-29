from flask import Blueprint,render_template

quiz=Blueprint('quiz',__name__)

@quiz.route('/attempt/<quiz_id>')
def attempt_quiz(quiz_id):
  return render_template('quiz.html',quiz_id=quiz_id)
  

