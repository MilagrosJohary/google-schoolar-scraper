from flask import Flask, render_template, request
from scrapper import search_user

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name')
    users = search_user(name)
    return render_template("home.html", users=users)