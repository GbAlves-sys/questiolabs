from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/about')
def about():
    return render_template('main/about.html')

@main_bp.route('/help')
def help():
    return render_template('main/help.html')

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('main/home.html')