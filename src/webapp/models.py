from . import establish_sql_connection
from flask_login import UserMixin
import uuid, bcrypt
from datetime import datetime

db_connection = establish_sql_connection()


def create_user_table():
    cursor = db_connection.cursor()
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
        id varchar(255) PRIMARY KEY,
        username varchar(255),
        email varchar(55),
        password varchar(55)
    );
    """)

    db_connection.commit()

class User(UserMixin):
    create_user_table()

    id: uuid
    username: str
    email: str
    password_hash: str

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.hash_password)
    
    
def create_note_table():
    cursor = db_connection.cursor()
    
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
    
class Note():
    create_note_table()
    
    id: uuid
    user_id: uuid
    note_title: str
    created_at: datetime
    content: str