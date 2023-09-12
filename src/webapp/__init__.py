from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
import random, string, os, psycopg2
from .views import views
from .auth import auth
from .models import User, Note
from .database import establish_sql_connection, get_user_by_email

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

login_manager = LoginManager()
@login_manager.user_loader
def load_user(email: str) -> User:
    user = get_user_by_email(email)
    return user

def generate_secret(length) -> str:
    return "".join(
        random.choice(string.ascii_lowercase) for i in range(length)
        )

def initialize_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    
    if not SECRET_KEY:
        app.config["SECRET_KEY"] = generate_secret(random.randint(12, 30))
    else:
        app.config["SECRET_KEY"] = SECRET_KEY
    
    establish_sql_connection()

    # registeres the blueprint
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app
