from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

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