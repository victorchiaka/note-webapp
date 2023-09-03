from dotenv import load_dotenv
from flask import Flask
import random, string, os

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
        
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")
    
    return app