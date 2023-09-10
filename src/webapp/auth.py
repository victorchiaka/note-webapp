from flask import Blueprint, render_template, request, flash
from flask_login import login_user, LoginManager
from .models import User
import uuid, bcrypt
from .database import get_user_by_email, create_new_user


auth = Blueprint("auth", __name__)

login_manager = LoginManager()

def is_email_taken(email: str) -> bool:
    user = get_user_by_email(email)
    return True if user else False

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirmpassword")

        if len(email) < 6:
            flash("Email must be at least 6 charcters", "warning")
            
        elif is_email_taken(email):
            flash("Email already taken", "error")

        elif len(username) < 3:
            flash("Username must be at least 3 charcters", "warning")

        elif password != confirm_password:
            flash("Passwords don't match", "error")

        elif len(password) < 4 or len(confirm_password) < 4:
            flash("Password or Confirm password must be at least 4 characters", "error")

        else:
            new_user = User(
                id=uuid.uuid4(),
                username=username,
                email=email,
                password_hash=bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt())
            )
            
            create_new_user(new_user)
            
            login_user(new_user)
            
            flash("account successfully created", "success")

    return render_template("signup.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return ""
