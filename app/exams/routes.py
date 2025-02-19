from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Exam, Question, Tag, db
import random

exams_bp = Blueprint('exams', __name__)

@exams_bp.route('/')
@login_required
def list_exams():
    exams = Exam.query.filter_by(user_id=current_user.id).all()
    return render_template('exams/list.html', exams=exams)

@exams_bp.route('/preview/<int:exam_id>')
@login_required
def preview_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    shuffled_questions = list(exam.questions)  # Converta para lista para permitir embaralhamento
    random.shuffle(shuffled_questions)  # Embaralha a ordem das questões
    
    # Embaralha as alternativas de cada questão objetiva
    for question in shuffled_questions:
        if question.type == "objetiva":
            # Passo 1: Converta as alternativas em uma lista de pares (letra, conteúdo)
            alternatives = list(question.alternatives.items())
            
            # Passo 2: Embaralhe as alternativas
            random.shuffle(alternatives)
            
            # Passo 3: Mantenha o gabarito correto após o embaralhamento
            # Encontre o conteúdo da alternativa correta original
            correct_content = question.alternatives.get(question.correct_answer, "")
            
            # Passo 4: Atualize o gabarito para a nova letra correspondente
            for idx, (letter, content) in enumerate(alternatives, start=1):
                if content == correct_content:
                    question.correct_answer = letter  # Atualiza a letra correta
                    break
            
            # Passo 5: Converta de volta para dicionário
            question.alternatives = dict(alternatives)
    
    return render_template('exams/preview.html', exam=exam, questions=shuffled_questions)
