from dotenv import load_dotenv
from flask import Flask
import random, string, os, psycopg2
from .views import views
from .auth import auth

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

# def establish_sql_connection():
#     DB_HOST = os.getenv("DB_HOST")
#     DB_NAME = os.getenv("DB_NAME")
#     DB_USER = os.getenv("DB_USER")
#     DB_PASSWORD = os.getenv("DB_PASSWORD")
    
#     return psycopg2.connect(
#         DB_HOST,
#         DB_NAME,
#         DB_USER,
#         DB_PASSWORD
#     )
    
# db_connection = establish_sql_connection()

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
        
    # registeres the blueprint
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app
