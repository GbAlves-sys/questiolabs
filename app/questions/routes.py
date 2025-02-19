from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Question, Tag, db
from datetime import datetime

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/create/objective', methods=['GET', 'POST'])
@login_required
def create_objective():
    if request.method == 'POST':
        try:
            # Capturar dados do formulário
            support = request.form.get('support')
            command = request.form.get('command')
            alternatives = {
                "A": request.form.get('alt1'),
                "B": request.form.get('alt2'),
                "C": request.form.get('alt3'),
                "D": request.form.get('alt4'),
                "E": request.form.get('alt5')
            }
            correct_answer = request.form.get('correct_answer')

            # Criar questão
            new_question = Question(
                title=f"Questão {datetime.now().strftime('%Y%m%d%H%M%S')}",  # Título temporário
                type="objetiva",
                support=support,
                command=command,
                alternatives=alternatives,
                correct_answer=correct_answer,
                user_id=current_user.id
            )

            # Adicionar tags (exemplo: separadas por vírgula)
            tags = request.form.get('tags', '').split(',')
            for tag_name in tags:
                tag = Tag.query.filter_by(name=tag_name.strip()).first()
                if not tag:
                    tag = Tag(name=tag_name.strip())
                    db.session.add(tag)
                new_question.tags.append(tag)

            db.session.add(new_question)
            db.session.commit()
            flash('Questão salva com sucesso!', 'success')
            return redirect(url_for('questions.list_questions'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao salvar: {str(e)}', 'danger')

    return render_template('questions/create_objective.html')

@questions_bp.route('/questions')
@login_required
def list_questions():
    questions = Question.query.all()
    return render_template('questions/list.html', questions=questions)