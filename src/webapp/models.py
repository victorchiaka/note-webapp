from flask_login import UserMixin
import uuid, bcrypt
from datetime import datetime

class User(UserMixin):
    id: uuid
    username: str
    email: str
    password_hash: str

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.hash_password)
    
class Note():
    
    id: uuid
    user_id: uuid
    note_title: str
    created_at: datetime
    content: str