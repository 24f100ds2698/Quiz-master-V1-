from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizmaster.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User 

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  

    from .routes import main
    from .admin_routes import admin
    from .user_routes import user
    from .quiz_routes import quiz

    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(quiz, url_prefix='/quiz')

    return app  




