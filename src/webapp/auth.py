from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

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
        
        elif len(username) < 3:
            flash("Username must be at least 3 charcters", "warning")
        
        elif password != confirm_password:
            flash("Passwords don't match", "error")
            
        elif len(password) < 4 or len(confirm_password) < 4:
            flash("Password or Confirm password must be at least 4 characters", "error")

        else: flash("account successfully created", "success")
        
    return render_template("signup.html")

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return ""
