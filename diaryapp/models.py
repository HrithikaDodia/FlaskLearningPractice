from datetime import datetime
from diaryapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(25), unique = True, nullable = False)
	email = db.Column(db.String(100), unique = True, nullable = False)
	image_file = db.Column(db.String(25), default = 'default.jpg', nullable = False)
	password = db.Column(db.String(60), nullable = False)
	pages = db.relationship('Page', backref='author', lazy=True)

	def __repr__(self):
		return self.username

class Page(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), primary_key = True)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	text_content = db.Column(db.Text, nullable = False)
	image = db.Column(db.String(25), nullable = True)
	video = db.Column(db.String(25), nullable = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

	def __repr__(self):
		return self.title