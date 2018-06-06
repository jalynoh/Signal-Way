import os
import secrets
from functools import wraps
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message

# Self developed imports
from signalapp import app, db, bcrypt, mail
from signalapp.models import User, Button
from signalapp.forms import LoginForm, InviteUserForm, InvitedCreationForm


# Login Page
@app.route("/", methods=['GET', 'POST'])
def login():
	# Verifies user is logged out
	if (current_user.is_authenticated):
		return (redirect(url_for('home')))

	form = LoginForm()

	if (form.validate_on_submit()):
		user = User.query.filter_by(email=form.email.data).first()
		if (user and bcrypt.check_password_hash(user.password, form.password.data)):
			login_user(user, remember=form.remember.data)
			return (redirect(url_for('home')))
		else:
			flash('Login unsuccessful. Please check email and password')

	return (render_template('login.html', form=form))

# Logout
@app.route("/logout")
def logout():
	logout_user()
	return (redirect(url_for('login')))

# Home Page
@app.route("/home")
@login_required
def home():
	return (render_template('home.html'))

# Admin Panel
@app.route("/admin")
@login_required
def admin():
	if (User.get_user_role(current_user) != 'admin'):
		return (render_template('home.html'))

	return (render_template('admin.html', title='Administrative'))

# User Invatation Page
@app.route("/invite", methods=['GET', 'POST'])
@login_required
def invite():
	if (User.get_user_role(current_user) != 'admin'):
		return (render_template('home.html'))

	form = InviteUserForm()
	if (form.validate_on_submit()):
		user = User(email=form.email.data)
		db.session.add(user)
		db.session.commit()
		send_invite_email(user)

		flash('User has been invited')
		return (redirect('admin'))

	return (render_template('invite.html', form=form, title='Invite User'))



def send_invite_email(user):
	token = user.get_invite_token()

	msg = Message('Invatation to Signal Way', sender='noreply@signalway.com', recipients=[user.email])
	msg.body = f'''
	You have been invited to join Signal Way, please use the following link to sign up:
	{ url_for('invited_creation', token=token, _external=True) }
	'''

	mail.send(msg)


@app.route("/user_creation/<token>", methods=['GET', 'POST'])
def invited_creation(token):
	if current_user.is_authenticated:
		return (redirect(url_for('logout')))

	user = User.verify_invite_token(token)

	if user is None:
		flash('Expired token')
		return (redirect(url_for('login')))

	form = InvitedCreationForm()
	if (form.validate_on_submit()):
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		user.first_name = form.first_name.data
		user.last_name = form.last_name.data
		db.session.commit()

		return (redirect(url_for('login')))

	return (render_template('invatation_creation.html', form=form, title='Registration'))




























