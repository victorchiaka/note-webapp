from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/home/<name>")
def home(name: str):
    return render_template("home.html", name=name)