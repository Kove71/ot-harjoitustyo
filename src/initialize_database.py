from database_connection import get_connection

conn = get_connection()

def drop_table():
    conn.execute("DROP TABLE if exists Movies")

def create_table():
    conn.execute('''CREATE TABLE if not exists Movies
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

if __name__ == "__main__":

    drop_table()
    create_table()
