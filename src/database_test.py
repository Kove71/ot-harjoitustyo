import sqlite3
from config import database_file_path

# Väliaikainen luokka, jonka tarkoitus on testata tietokannan toimivuutta. Toimii.

class DatabaseConnection:

    def __init__(self):


        self.conn = sqlite3.connect(database_file_path)
        self.conn.isolation_level = None
    
    #Kutsutaan kun halutaan alustaa taulu/tietokanta. Tarkistaa jos ei ole jo kyseistä taulua ja luo sen.
    
    def create_table(self):
        self.conn.execute('''CREATE TABLE if not exists Movies
            (id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            poster TEXT NOT NULL,
            imdb_id TEXT NOT NULL,
            release_date TEXT NOT NULL,
            review INT);''')

#Tämän osan testaukseen
if __name__ == "__main__":
    connection = DatabaseConnection()
    connection.create_table()
