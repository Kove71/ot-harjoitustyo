import unittest
from services.imdb_api import IMDBSearch

#Testaa toistaiseksi vain IMDBSearch-luokan request.search()-metodia

class TestIMDBSearch(unittest.TestCase):

    def setUp(self):
        self.search = IMDBSearch()

    def test_search_with_searchword(self):
        length = len(self.search.request_search("salo"))
        self.assertGreaterEqual(length, 1)

    def test_search_without_searchword(self):
        length = len(self.search.request_search(""))
        self.assertEqual(length, 0)

    def test_search_with_zero_results(self):
        length = len(self.search.request_search("zibazubazei"))
        self.assertEqual(length, 0)
