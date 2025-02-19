from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Define a rota de login padrão para redirecionamento
    login_manager.login_view = "auth.login"

    # Importa e registra os blueprints
    from app.auth import auth_bp
    from app.routes import main_bp
    from app.questions import questions_bp  # Importa o blueprint de questões
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(questions_bp)  # Registra o blueprint de questões

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))