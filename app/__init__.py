from flask import Flask 
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
	return "index page"
@app.route("/hello/")
def helloWorld():
	return  "<p>Hello flask</p>"

@app.route("/user")
def user():
	return "user page"

@app.route("/user/<username>/") 
def show_user_profile(username):
	return f"hello {escape(username)}"

