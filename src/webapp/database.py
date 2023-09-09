import os, psycopg2
from dotenv import load_dotenv

load_dotenv()

def establish_sql_connection():
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