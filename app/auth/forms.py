from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired(),
        Length(min=4, max=20, message="O usuário deve ter entre 4 e 20 caracteres")
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(),
        Length(min=6, message="A senha deve ter no mínimo 6 caracteres")
    ])
    confirm_password = PasswordField('Confirmar Senha', validators=[
        DataRequired(),
        EqualTo('password', message="As senhas não coincidem")
    ])
    submit = SubmitField('Registrar')

    # Validação customizada: usuário único
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este usuário já está em uso. Escolha outro.')