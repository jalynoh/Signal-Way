from flask import Flask
from signalapp.config import Config
# from flask_sqlalchemy import SQLAlchemy  # DB integration library (see models.py)

# User login specific modules
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager



# Instantiations
# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'  # Login route function



def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	# Initializations
	# db.init_app(app)
	# bcrypt.init_app(app)
	# login_manager.init_app(app)

	# Blueprint setup
	from signalapp.main.routes import main
	app.register_blueprint(main)
	
	# from signal.users.routes import users
	# app.register_blueprint(users)

	# from signal.errors.handlers import errors
	# app.register_blueprint(errors)


	return app

