from flask_login import UserMixin
import uuid, bcrypt
from datetime import datetime


class User(UserMixin):
    def __init__(
        self, id: uuid, username: str, email: str, password_hash: bytes
    ) -> None:
        self.id: uuid = id
        self.username: str = username
        self.email: str = email
        self.password_hash: str = password_hash

    @classmethod
    def get_instance(
        cls, id: uuid, username: str, email: str, password_hash: bytes
    ) -> "User":
        return cls(id, username, email, password_hash)

    def is_valid_password(self, password: str):
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )


class Note:
    def __init__(
        self, id: uuid, user_id: uuid, title: str, content: str, created_at: datetime
    ) -> None:
        self.id: uuid = id
        self.user_id: uuid = user_id
        self.title: str = title
        self.content: str = content
        self.created_at: datetime = created_at

    @classmethod
    def get_instance(
        cls,
        id: uuid,
        user_id: uuid,
        title: str,
        content: str,
        created_at: datetime,
    ) -> "Note":
        return cls(id, user_id, title, content, created_at)
