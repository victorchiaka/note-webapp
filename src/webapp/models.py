from . import establish_sql_connection
from flask_login import UserMixin
import uuid, bcrypt


db_connection = establish_sql_connection()

cursor = db_connection.cursor()

create_table = """
CREATE TABLE IF NOT EXIST user (
    id varchar(255) PRIMARY KEY,
    username varchar(255),
    email varchar(55),
    password varchar(55)
);
"""

cursor.execute(create_table)

class User(UserMixin):
    def __init__(self, username: str, email: str, password: str) -> None:
        id = uuid.uuid4()
        self.username = username
        self.email = email
        self.password_hash = self.hash_password(password)
        
    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        
    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.hash_password)