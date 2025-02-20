from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import Question, Tag, Skill
from app import db

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    tag_filter = request.args.get('tag', None, type=str)
    skill_filter = request.args.get('skill', None, type=str)
    question_type = request.args.get('type', None, type=str)

    query = Question.query

    if tag_filter:
        query = query.join(Question.tags).filter(Tag.name == tag_filter)
    if skill_filter:
        query = query.join(Question.skills).filter(Skill.name == skill_filter)
    if question_type:
        query = query.filter(Question.type == question_type)

    questions = query.paginate(page=page, per_page=10)
    
    tags = Tag.query.all()
    skills = Skill.query.all()
    
    return render_template('questions/index.html', questions=questions, tags=tags, skills=skills)

@questions_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        type = request.form['type']
        command = request.form['command']  # Suporte a rich text
        answer_key = request.form['answer_key']
        support_text = request.form.get('support_text', '')

        question = Question(
            type=type,
            command=command,
            answer_key=answer_key,
            support_text=support_text
        )

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

        db.session.add(question)
        db.session.commit()

        flash('Questão criada com sucesso!', 'success')
        return redirect(url_for('questions.index'))

    tags = Tag.query.all()
    skills = Skill.query.all()
    return render_template('questions/create.html', tags=tags, skills=skills)

@questions_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    question = Question.query.get_or_404(id)
    if request.method == 'POST':
        question.type = request.form['type']
        question.command = request.form['command']  # Suporte a rich text
        question.answer_key = request.form['answer_key']
        question.support_text = request.form.get('support_text', '')

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

    tags = Tag.query.all()
    skills = Skill.query.all()
    return render_template('questions/edit.html', question=question, tags=tags, skills=skills)

@questions_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    flash('Questão excluída com sucesso!', 'success')
    return redirect(url_for('questions.index'))
