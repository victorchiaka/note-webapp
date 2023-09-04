from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "" # suppose to return a redirect to "/" after login the user out
