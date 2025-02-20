from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import Exam, Question
from app import db

exams_bp = Blueprint('exams', __name__)

@exams_bp.route('/')
@login_required
def index():
    # Lista todas as provas (com paginação e filtros no futuro)
    exams = Exam.query.all()
    return render_template('exams/index.html', exams=exams)

@exams_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Lógica para criar uma nova prova
        name = request.form['name']
        questions = request.form.getlist('questions')

        # Cria a prova
        exam = Exam(name=name)

        # Adiciona as questões selecionadas à prova
        for question_id in questions:
            question = Question.query.get(question_id)
            if question:
                exam.questions.append(question)

        # Salva a prova no banco de dados
        db.session.add(exam)
        db.session.commit()

        flash('Prova criada com sucesso!', 'success')
        return redirect(url_for('exams.index'))

    # Lista todas as questões para seleção
    questions = Question.query.all()
    return render_template('exams/create.html', questions=questions)

@exams_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    exam = Exam.query.get_or_404(id)
    if request.method == 'POST':
        # Lógica para editar a prova
        exam.name = request.form['name']
        exam.questions = []

        questions = request.form.getlist('questions')
        for question_id in questions:
            question = Question.query.get(question_id)
            if question:
                exam.questions.append(question)

        db.session.commit()
        flash('Prova atualizada com sucesso!', 'success')
        return redirect(url_for('exams.index'))

    questions = Question.query.all()
    return render_template('exams/edit.html', exam=exam, questions=questions)

@exams_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    exam = Exam.query.get_or_404(id)
    db.session.delete(exam)
    db.session.commit()
    flash('Prova excluída com sucesso!', 'success')
    return redirect(url_for('exams.index'))