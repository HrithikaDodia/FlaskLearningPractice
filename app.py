from flask import Flask, render_template, flash, url_for, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '62582fc136cac3457137050bc8d857c4'

posts = [
	{
		'author': 'abc',
		'title': 'Blog Post',
		'content': 'First Post',
		'date_posted': 'March 5, 2000'
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account Created')
		return redirect(url_for('home'))
	return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('login.html', form = form)


if __name__ == '__main__':
	app.run(debug = True)