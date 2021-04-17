import sqlite3
from config import database_file_path

def get_connection():
    conn = sqlite3.connect(database_file_path)
    conn.isolation_level = None
    return conn