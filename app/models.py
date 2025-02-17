from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Tabela de associação para Questão <-> Tag (relação muitos-para-muitos)
question_tags = db.Table(
    'question_tags',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Correção aqui: parêntese fechado corretamente
    type = db.Column(db.String(20), nullable=False)  # "objetiva" ou "discursiva"
    support = db.Column(db.Text, nullable=False)  # Recurso de apoio (HTML)
    command = db.Column(db.Text, nullable=False)  # Comando (HTML)
    alternatives = db.Column(db.JSON)  # Armazena alternativas como JSON
    correct_answer = db.Column(db.String(10), nullable=False)  # Letra (A-E) ou texto
    tags = db.relationship('Tag', secondary=question_tags, backref='questions')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Questão '{self.title}'"