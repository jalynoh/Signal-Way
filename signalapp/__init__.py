import os
import local_envars
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Flask DB Integration
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_mail import Mail

# Local enviornment variables for testing
local_envars.set_variables()

# Configurations
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Only for debugging to update CSS
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']  # Used to prevent CSRF
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
# Mail Configurations
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = int(os.environ['MAIL_PORT'])
app.config['MAIL_USE_TLS'] = True  # Email encryption
app.config['MAIL_USERNAME'] = os.environ['EMAIL']
app.config['MAIL_PASSWORD'] = os.environ['PASS']



# Instantiations
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

# Flask login settings
login_manager.login_view = 'login'




from signalapp import routes  # To prevnt potential circular imports