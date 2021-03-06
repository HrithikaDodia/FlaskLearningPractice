from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from diaryapp.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired(), Length(min = 8)])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), 
										EqualTo('password')])
	submit = SubmitField('Sign Up')

# Not included in templates yet!
	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('Username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('Email already exists')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')