import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Flask DB Integration
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# Configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsAKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# Instantiations
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

# Flask login settings
login_manager.login_view = 'login'


from signalapp import routes  # To prevnt potential circular imports