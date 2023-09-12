import os, psycopg2
from dotenv import load_dotenv
from .models import User

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

db_connection = psycopg2.connect(
    database=DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

def establish_sql_connection():
    
    cursor = db_connection.cursor()
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
        id varchar(255) PRIMARY KEY,
        username varchar(255),
        email varchar(255),
        password_hash varchar(455)
    );
    """)
    
    db_connection.commit()
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
        id varchar(255) PRIMARY KEY,
        user_id varchar(255),
        FOREIGN KEY (user_id) REFERENCES users(id),
        note_title varchar(35),
        content varchar(10000)
    );
    """)

    db_connection.commit()
    
    return db_connection

def get_user_by_email(email: str) -> User | None:
    cursor = db_connection.cursor()
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    data = cursor.fetchone()
    
    if data is None:
        return None
    
    user = User(id=data[0], username=data[1], email=data[2], password_hash=(data[3])[2:-1])
    
    return user


def create_new_user(user: User):
    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO users (id, username, email, password_hash) VALUES (%s, %s, %s, %s)",
        (str(user.id), user.username,  user.email, user.password_hash)
    )
    
    db_connection.commit()