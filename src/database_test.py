import sqlite3

class DatabaseConnection:

    def __init__(self):
        self.conn = sqlite3.connect("../data/database.db")
        self.conn.isolation_level = None
    
    def create_table(self):
        self.conn.execute('''CREATE TABLE if not exists Movies
            (id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            poster TEXT NOT NULL,
            imdb_id TEXT NOT NULL,
            release_date TEXT NOT NULL,
            review INT);''')

#for testing functionality
if __name__ == "__main__":
    connection = DatabaseConnection()
    connection.create_table()