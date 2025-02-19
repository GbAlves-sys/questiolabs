from flask import Blueprint, render_template
from flask_login import login_required

# Cria o blueprint para as rotas principais
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def home():
    return render_template('home.html')  