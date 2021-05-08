import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from database_connection import get_connection, get_test_connection #pylint: disable=wrong-import-position

class DatabaseActions:
    """Tietokannan toiminnasta vastuussa oleva luokka.
    Attributes:
        conn: yhteys tietokantaan
        cur: kursori, jonka avulla tehdään SQL-kyselyitä
    """

    def __init__(self, test = False):
        """Luokan konstrukotori, alustaa yhteyden tietokantaan.

        Args:
            test: boolean, jolla katsotaan onko yhteys testi-tietokantaan
                tai varsinaiseen tietokantaan.
        """

        if test:
            self.conn = get_test_connection()
        else:
            self.conn = get_connection()
        self.cur = self.conn.cursor()

    def add_movie_to_database(self, selected_movie):
        """Lisää elokuvan tietokantaan

        Args:
            selected_movie: Luokan MovieDetails tieto-objekti, jossa on tietokantaan
                lisättävät tiedot.
        """

        self.conn.execute("INSERT INTO Movies \
            (title, poster, imdb_id, release_date, director, avg_rating, length, length_mins) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                selected_movie.title, selected_movie.poster,
                selected_movie.id, selected_movie.release_date,
                selected_movie.director, selected_movie.avg_rating,
                selected_movie.length, selected_movie.length_mins])

        return True

    def select_movies(self):
        """Valitsee elokuvat tietokannasta ja palauttaa ne käyttöliittymälle.
        """

        self.cur.execute("SELECT id, title, release_date, director, \
            avg_rating, length_mins, review, watched FROM Movies")
        rows = self.cur
        movies = []
        for row in rows:
            movies.append(row)
        return movies

    def update_data(self, movie_id, review, watch_date):
        """Päivittää annetun elokuvan katsomispäivän ja arvostelun.

        Args:
            movie_id: elokuvan tietokanta-id
            review: arvostelu
            watch_date: katsomispäivä
        """

        self.cur.execute("UPDATE Movies SET review=?, watched=? WHERE id=?", [
            review, watch_date, movie_id
        ])

    def delete_row(self, movie_id):
        """Poistaa annetun elokuvan tietokannasta

        Args:
            movie_id: elokuvan tietokanta-id
        """

        self.cur.execute("DELETE FROM Movies WHERE id =?", [movie_id])
