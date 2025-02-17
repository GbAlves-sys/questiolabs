from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user
from matplotlib.colors import LogNorm
from app.models import User
from app import db
from .forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))  # Redireciona para 'main.home'
        flash('Usuário ou senha inválidos!', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        try:
            # Cria usuário e salva no banco
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('auth.login'))
        
        except Exception as e:
            db.session.rollback()
            flash('Erro ao criar a conta. Tente novamente.', 'danger')
    
    return render_template('auth/register.html', form=form)