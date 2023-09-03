from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def index():
    # return "<h1>Hello</h1>"
    return render_template("index.html")