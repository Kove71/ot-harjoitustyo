import unittest
from services.imdb_api import IMDBSearch
from database_connection import get_test_connection

class TestIMDBSearch(unittest.TestCase):

    def setUp(self):
        self.search = IMDBSearch()
        self.con = get_test_connection()
        self.cur = self.con.cursor()

    def test_search_with_searchword(self):
        length = len(self.search.request_search("salo"))
        self.assertGreaterEqual(length, 1)

    def test_search_without_searchword(self):
        length = len(self.search.request_search(""))
        self.assertEqual(length, 0)

    def test_search_with_zero_results(self):
        length = len(self.search.request_search("zibazubazei"))
        self.assertEqual(length, 0)

    def test_request_title(self):
        imdb_id = "tt1375666"
        self.search.request_title(imdb_id, True)
        title = self.cur.execute("SELECT title FROM Movies").fetchone()
        self.assertEqual(title[0], "Inception")
