from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from app.main.routes import main_bp
from app.questions.routes import questions_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar blueprints e modelos depois para evitar dependência circular
from app.auth.routes import auth_bp
from app.models import User

app.register_blueprint(auth_bp)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

from app.questions.routes import questions_bp

app.register_blueprint(questions_bp, url_prefix='/questions')

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Rota de login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(main_bp)

app.register_blueprint(questions_bp, url_prefix='/questions')  
