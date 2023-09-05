from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm-password")
        

    return render_template("signup.html")

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "" # suppose to return a redirect to "/" after login the user out
