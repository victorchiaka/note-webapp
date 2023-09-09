from dotenv import load_dotenv
from flask import Flask
import random, string, os, psycopg2
from .views import views
from .auth import auth

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def generate_secret(length):
    return "".join(
        random.choice(string.ascii_lowercase) for i in range(length)
        )

def initialize_app():
    
    app = Flask(__name__)
    if not SECRET_KEY:
        app.config["SECRET_KEY"] = generate_secret(random.randint(12, 30))
    else:
        app.config["SECRET_KEY"] = SECRET_KEY
        
    from .database import establish_sql_connection
    from .models import User, Note
    
    establish_sql_connection()

    # registeres the blueprint
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app
