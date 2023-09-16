from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import (
    current_user,
    login_user,
    login_required,
    logout_user,
    LoginManager,
)
from .models import User
import uuid, bcrypt
from .database import get_user_by_email, create_new_user
from .utils import is_email_taken

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form
        username: str = data.get("username")
        email: str = data.get("email")
        password: str = data.get("password")
        confirm_password: str = data.get("confirmpassword")

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
            new_user: User = User(
                id=uuid.uuid4(),
                username=username,
                email=email,
                password_hash=str(
                    bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
                ),
            )

            create_new_user(new_user)

            login_user(new_user, remember=True)

            flash("account successfully created", "success")

            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username: str = request.form.get("username")
        email: str = request.form.get("email")
        password: str = request.form.get("password")

        user = get_user_by_email(email)

        if not user:
            flash("user with this email does not exist", "error")
        else:
            if username != user.username:
                flash("invalid username field", "warning")
            elif not user.is_valid_password(password):
                flash("invalid password", "warning")
            else:
                login_user(user, remember=True)
                flash("login successful", "success")
                return redirect(url_for("views.home"))

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("successfully logged out", "success")
    return redirect(url_for("auth.login"))
