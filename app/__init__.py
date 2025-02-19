from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # Adicione essa importação
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()  # Inicializa o LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)  # Inicializa o LoginManager no app

    # Define a rota de login padrão para redirecionamento
    login_manager.login_view = "auth.login"

    # Importa e registra os blueprints
    from app.auth import auth_bp
    from app.routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Importação dentro da função para evitar import circular
    return User.query.get(int(user_id))  # Retorna o usuário pelo ID