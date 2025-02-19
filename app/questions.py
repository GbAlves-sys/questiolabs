from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import Question, Tag, Skill
from app import db

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/')
@login_required
def index():
    # Lista todas as questões (com paginação e filtros no futuro)
    questions = Question.query.all()
    return render_template('questions/index.html', questions=questions)

@questions_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Lógica para criar uma nova questão
        type = request.form['type']
        command = request.form['command']
        answer_key = request.form['answer_key']
        support_text = request.form.get('support_text', '')

        # Cria a questão
        question = Question(
            type=type,
            command=command,
            answer_key=answer_key,
            support_text=support_text
        )

        # Adiciona tags e habilidades (se houver)
        tags = request.form.getlist('tags')
        skills = request.form.getlist('skills')

        for tag_name in tags:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            question.tags.append(tag)

        for skill_name in skills:
            skill = Skill.query.filter_by(name=skill_name).first()
            if not skill:
                skill = Skill(name=skill_name)
            question.skills.append(skill)

        # Salva a questão no banco de dados
        db.session.add(question)
        db.session.commit()

        flash('Questão criada com sucesso!', 'success')
        return redirect(url_for('questions.index'))

    return render_template('questions/create.html')

@questions_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    question = Question.query.get_or_404(id)
    if request.method == 'POST':
        # Lógica para editar a questão
        question.type = request.form['type']
        question.command = request.form['command']
        question.answer_key = request.form['answer_key']
        question.support_text = request.form.get('support_text', '')

        # Atualiza tags e habilidades
        question.tags = []
        question.skills = []

        tags = request.form.getlist('tags')
        skills = request.form.getlist('skills')

        for tag_name in tags:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            question.tags.append(tag)

        for skill_name in skills:
            skill = Skill.query.filter_by(name=skill_name).first()
            if not skill:
                skill = Skill(name=skill_name)
            question.skills.append(skill)

        db.session.commit()
        flash('Questão atualizada com sucesso!', 'success')
        return redirect(url_for('questions.index'))

    return render_template('questions/edit.html', question=question)

@questions_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    flash('Questão excluída com sucesso!', 'success')
    return redirect(url_for('questions.index'))