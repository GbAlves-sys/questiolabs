from flask import Blueprint, render_template

exams_bp = Blueprint('exams', __name__)

@exams_bp.route('/')
def index():
    return render_template('exams/index.html')
