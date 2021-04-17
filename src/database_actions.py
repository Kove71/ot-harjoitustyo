import sqlite3
from database_connection import get_connection

class DatabaseActions:

    def __init__(self):
        self.conn = get_connection()
            
    def add_movie_to_database(self, selected_movie):
        self.conn.execute("INSERT INTO Movies (title, poster, imdb_id, release_date, director, avg_rating, length, length_mins) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [selected_movie.title, 
            selected_movie.poster, 
            selected_movie.id, 
            selected_movie.release_date, 
            selected_movie.director,
            selected_movie.avg_rating,
            selected_movie.length,
            selected_movie.length_mins
            ])      

        return True      
