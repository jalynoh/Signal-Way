from flask import render_template
from signalapp import app


# Home Page
@app.route("/")
@app.route("/home")
def home():
	return ("Hello")