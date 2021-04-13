import unittest
from imdb_search import IMDBSearch

#Testaa toistaiseksi vain IMDBSearch-luokan request.search()-metodia

class TestIMDBSearch(unittest.TestCase):

    def setUp(self):
        self.search = IMDBSearch()

    def test_search_with_searchword(self):
        self.assertEqual(self.search.request_search("salo"), True)
    
    def test_search_without_searchword(self):
        self.assertEqual(self.search.request_search(""), False)

    def test_search_with_zero_results(self):
        self.assertEqual(self.search.request_search("zibazubazei"), False)
