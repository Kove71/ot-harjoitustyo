import sqlite3
from database_connection import get_connection

class DatabaseInit:

    def __init__(self):
        self.conn = get_connection()
        self.drop_table()

    def drop_table(self):
        self.conn.execute("DROP TABLE if exists Movies")
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE if not exists Movies
            (id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            poster TEXT,
            imdb_id TEXT,
            release_date TEXT,
            avg_rating TEXT,
            director TEXT,
            length TEXT,
            length_mins INTEGER,
            review INT,
            watched TEXT);''')