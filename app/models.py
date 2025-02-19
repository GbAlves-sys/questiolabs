from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Tabela de associação para relação muitos-para-muitos entre Questão e Tag
question_tags = db.Table('question_tags',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

# Tabela de associação para relação muitos-para-muitos entre Questão e Habilidade
question_skills = db.Table('question_skills',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # 'objective' ou 'discursive'
    support_text = db.Column(db.Text, nullable=True)  # Recurso de apoio
    command = db.Column(db.Text, nullable=False)  # Comando da questão
    answer_key = db.Column(db.Text, nullable=False)  # Gabarito
    alternatives = db.relationship('Alternative', backref='question', lazy=True)  # Alternativas (apenas para questões objetivas)
    tags = db.relationship('Tag', secondary=question_tags, lazy='subquery', backref=db.backref('questions', lazy=True))
    skills = db.relationship('Skill', secondary=question_skills, lazy='subquery', backref=db.backref('questions', lazy=True))

class Alternative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)  # Texto da alternativa
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)