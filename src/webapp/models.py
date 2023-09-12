from flask_login import UserMixin
import uuid, bcrypt
from datetime import datetime

class User(UserMixin):
    def __init__(self, id: uuid, username: str, email: str, password_hash: bytes) -> None:
        self.id: uuid = id
        self.username: str = username
        self.email: str = email
        self.password_hash: str = password_hash

    def is_valid_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash.encode("utf-8"))

class Note:
    id: uuid
    user_id: uuid
    note_title: str
    created_at: datetime
    content: str