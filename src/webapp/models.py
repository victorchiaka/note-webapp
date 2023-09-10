from flask_login import UserMixin
import uuid, bcrypt
from datetime import datetime

class User(UserMixin):
    def __init__(self, id, username, email, password_hash) -> None:
        self.id: uuid = id
        self.username: str = username
        self.email: str = email
        self.password_hash: str = password_hash

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.hash_password)
    
class Note:
    id: uuid
    user_id: uuid
    note_title: str
    created_at: datetime
    content: str