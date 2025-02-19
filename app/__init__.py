from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import db
from app.exams.routes import exams_bp  # Importando o blueprint dos exames
from app.auth.routes import auth_bp  # Importando o blueprint de autenticação

# Inicializando o banco de dados e o gerenciador de login
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)  # Inicializa o banco de dados
    login_manager.init_app(app)  # Inicializa o Flask-Login

    # Registra os blueprints
    app.register_blueprint(exams_bp, url_prefix='/exams')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
