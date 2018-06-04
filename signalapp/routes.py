import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message

# Self developed imports
from signalapp import app, db, bcrypt, mail
from signalapp.models import User, Button
from signalapp.forms import LoginForm, InviteUserForm


# Login Page
@app.route("/", methods=['GET', 'POST'])
def login():
	# Verifies user is logged out
	if (current_user.is_authenticated):
		return (url_for('home'))

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
	return (render_template('admin.html'))

# UTIL function for invite
def send_invite_email(email_addrs):
	token = email_addrs.get_invtie_token()
	msg = Message('SignalWay Invite', sender='invite@signalway.com', recipients=[email_addrs])
	msg.body = f'''
You have been invited to SignalWay, please use the following link to register:
{ url_for('register', token=token, _external=True) }

-SignalWay
				'''
	mail.send(msg)

# Invite User
@app.route("/admin/invite", methods=['GET', 'POST'])
@login_required
def invite():
	form = InviteUserForm()

	if (form.validate_on_submit()):
		send_invite_email(form.email.data)
		flash('User has been sent an invite link.')

	return (render_template('invite.html'))

@app.route('/register/<token>', methods=['GET', 'POST'])
def register():
	pass
	













