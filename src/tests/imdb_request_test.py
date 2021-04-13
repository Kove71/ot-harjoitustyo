import unittest
from imdb_search import IMDBSearch

class TestIMDBSearch(unittest.TestCase):

    def setUp(self):
        self.search = IMDBSearch()

    def test_search_with_searchword(self):
        self.assertEqual(self.search.request_search("up"), True)
    
    def test_search_without_searchword(self):
        self.assertEqual(self.search.request_search(""), False)

