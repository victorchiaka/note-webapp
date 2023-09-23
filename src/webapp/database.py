from dotenv import load_dotenv
from .models import Note, User
from typing import List, Tuple, Optional
import os, psycopg2, uuid
from datetime import datetime

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

db_connection = psycopg2.connect(
    database=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD
)


def establish_sql_connection():
    cursor = db_connection.cursor()

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS users (
        id varchar(255) PRIMARY KEY,
        username varchar(255),
        email varchar(255),
        password_hash varchar(455)
    );
    """
    )

    db_connection.commit()

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS notes (
        id varchar(255) PRIMARY KEY,
        user_id varchar(255),
        FOREIGN KEY (user_id) REFERENCES users(id),
        title varchar(35),
        content varchar(10000),
        created_at timestamp default current_timestamp
    );
    """
    )

    db_connection.commit()

    return db_connection


def get_user_by_email(email: str) -> Optional[User]:
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE email = %s;", (email,))
    data = cursor.fetchone()

    if data is None:
        return None
    user_id, username, email, hashed_password = data

    user = User.get_instance(
        id=user_id, username=username, email=email, password_hash=hashed_password[2:-1]
    )

    return user


def get_user_by_id(id: bytes) -> Optional[User]:
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id = %s;", (id,))
    data = cursor.fetchone()

    if data is None:
        return None
    user_id, username, email, hashed_password = data

    user = User.get_instance(
        id=user_id, username=username, email=email, password_hash=hashed_password[2:-1]
    )

    return user


def create_new_user(user: User):
    cursor = db_connection.cursor()

    cursor.execute(
        "INSERT INTO users (id, username, email, password_hash) VALUES (%s, %s, %s, %s);",
        (str(user.id), user.username, user.email, user.password_hash),
    )

    db_connection.commit()


def create_new_note(note: Note):
    cursor = db_connection.cursor()

    cursor.execute(
        "INSERT INTO notes (id, user_id, title, content, created_at) VALUES (%s, %s, %s, %s, %s)",
        (str(note.id), str(note.user_id), note.title, note.content, note.created_at),
    )

    db_connection.commit()


def get_all_notes(user_id: uuid) -> List[Note]:
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM notes where user_id = %s;", (str(user_id),))
    note_records: List[
        Tuple[uuid.UUID, uuid.UUID, str, str, datetime]
    ] = cursor.fetchall()
    notes: List[Note] = []

    for record in note_records:
        id, user_id, title, content, created_at = record

        note: Note = Note(id, user_id, title, content, created_at)

        notes.append(note)

    return notes


def delete_note_by_id(id: uuid):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM notes * WHERE id = %s;", (str(id),))

    db_connection.commit()


def get_note_by_id(id: uuid):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = %s;", (str(id),))

    id, user_id, title, content, created_at = cursor.fetchone()

    note: Note = Note(id, user_id, title, content, created_at)

    return note


def delete_account_by_id(id: uuid):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM users * WHERE id = %s;", (str(id),))

    db_connection.commit()

def delete_all_notes_by_user_id(user_id: uuid):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM notes * WHERE user_id = %s;", (str(user_id),))

    db_connection.commit()
