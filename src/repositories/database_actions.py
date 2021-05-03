import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from database_connection import get_connection, get_test_connection #pylint: disable=wrong-import-position

class DatabaseActions:

    def __init__(self, test = False):
        if test:
            self.conn = get_test_connection()
        else:
            self.conn = get_connection()
        self.cur = self.conn.cursor()

    def add_movie_to_database(self, selected_movie):
        self.conn.execute("INSERT INTO Movies \
            (title, poster, imdb_id, release_date, director, avg_rating, length, length_mins) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                selected_movie.title, selected_movie.poster,
                selected_movie.id, selected_movie.release_date,
                selected_movie.director, selected_movie.avg_rating,
                selected_movie.length, selected_movie.length_mins])

        return True

    def select_movies(self):
        self.cur.execute("SELECT id, title, release_date, director, \
            avg_rating, length_mins, review, watched FROM Movies")
        rows = self.cur
        movies = []
        for row in rows:
            movies.append(row)
        return movies
    
    def update_data(self, movie_id, review, watch_date):
        self.cur.execute("UPDATE Movies SET review=?, watched=? WHERE id=?", [
            review, watch_date, movie_id
        ])

    def delete_row(self, movie_id):
        self.cur.execute("DELETE FROM Movies WHERE id =?", [movie_id])