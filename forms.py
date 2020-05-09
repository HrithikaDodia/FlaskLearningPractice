from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired(), Length(min = 8)])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), 
										EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')