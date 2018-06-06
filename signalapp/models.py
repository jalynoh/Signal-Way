from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Self developed imports
from signalapp import db, login_manager, app


# UTIL methods
# Manages user sessions
@login_manager.user_loader
def load_user(user_id):
	return (User.query.get(int(user_id)))


# User table
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)

	# User information
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	role = db.Column(db.String(80), nullable=False)
	buttons_tested = db.relationship('Button', backref='tester', lazy=True)

	# User authentication
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False, default='signalway')

	def set_user_role(self, role):
		self.role = role

	def get_user_role(self):
		return (self.role)



# Panic button table
class Button(db.Model):
	__tablename__ = 'button'
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