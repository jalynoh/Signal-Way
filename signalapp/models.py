from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Self developed imports
from signalapp import db, login_manager, app


# Manages user sessions
@login_manager.user_loader
def load_user(user_id):
	return (User.query.get(int(user_id)))

def get_invite_token(expires_sec=1800):
	s = Serializer(app.config['SECRET_KEY'], expires_sec)
	return (s.dumps({'email_id': id}))


# User table
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False, default='signalway')
	buttons_tested = db.relationship('Button', backref='tester', lazy=True)

	def __repr__(self):
		return (f"User('{self.email}')")

class Button(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	district = db.Column(db.String(20), nullable=False)
	building = db.Column(db.String(160), nullable=False)
	location = db.Column(db.String(160), nullable=False)
	site = db.Column(db.String(20), nullable=False, default='unknown')
	code = db.Column(db.String(20), nullable=False, default='unknown')
	style = db.Column(db.String(20), nullable=False, default='unknown')
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	state = db.Column(db.String(20), nullable=False, default='unknown')
	last_return = db.Column(db.String(20), nullable=False, default='unknown')
	notes = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return (f"Button('{self.district}', '{self.building}', '{self.location}', '{self.site}', \
						'{self.code}', '{self.style}', '{self.date_created}', '{self.state}', \
						'{self.last_return}')")