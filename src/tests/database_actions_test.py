import unittest
from repositories.database_actions import DatabaseActions
from initialize_database import create_table
from database_connection import get_test_connection
from entities.movie_items import MovieDetails

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.test_case = True
        self.database = DatabaseActions(self.test_case)
        self.conn = get_test_connection()
        self.cur = self.conn.cursor()
        self.movie_details = {"title": "Inception",
            "releaseDate": "2010-07-14",
            "directors": "Christopher Nolan",
            "imDbRating": 	"8.8",
            "image": "photo",
            "runtimeStr": "2h 28mins",
            "runtimeMins": "148",
            "id": "tt1375666"}
        self.test_movie = MovieDetails(self.movie_details)

    def test_add_movie(self):
        create_table(self.test_case)
        self.database.add_movie_to_database(self.test_movie)
        title = self.cur.execute("SELECT title FROM Movies").fetchone()
        self.assertEqual(title[0], "Inception")

    def test_select_movies(self):
        create_table(self.test_case)
        movies = self.database.select_movies()
        self.assertEqual(type(movies), list)
