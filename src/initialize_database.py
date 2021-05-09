from database_connection import get_connection, get_test_connection


def drop_table(test = False):
    """Poistaa tietokannan Movies-taulukon

    Args:
        test: määrittelee onko yhteys testitietokantaan vai tavalliseen
    """

    if test:
        conn = get_test_connection()
    else:
        conn = get_connection()
    conn.execute("DROP TABLE if exists Movies")

def create_table(test = False):
    """Luo taulukon Movies

    Args:
        test: määrittelee onko yhteys testitietokantaan vai tavalliseen
    """

    if test:
        conn = get_test_connection()
    else:
        conn = get_connection()
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
