# coding: utf-8
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, PasswordField


class LoginForm(Form):
    email = StringField(u'电子邮件', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired()])
