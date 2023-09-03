from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/hello")
def index():
    return "<h1>Hello</h1>"

# @auth.route("login")
# def login():
#     return "<h1>Login</h1>"


# @auth.route("logout")
# def login():
#     return "<h1>Logout</h1>"