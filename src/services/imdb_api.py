import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

import requests # pylint: disable=wrong-import-position

from entities.movie_items import SearchMovie, MovieDetails # pylint: disable=wrong-import-position
from repositories.database_actions import DatabaseActions # pylint: disable=wrong-import-position


class IMDBSearch:
    """Luokka, joka on vastuussa API-kutsuista.

    Attributes:
        search_url: url-osoite elokuvahaun API-kutsuun
        title_url: url-osoite elokuvatietojen API-kutsuun
        movie_list: lista elokuvahaun tuloksista
        result_length: elokuvahaun tulosten määrä
    """
    
    def __init__(self):
        """Luokan konstruktori
        """

        self.search_url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"
        self.title_url = "https://imdb-api.com/en/API/Title/k_grjsr7l7/"
        self.movie_list = []
        self.result_length = 0

    def request_search(self, searchword: str):
        """Hakee elouvat käyttäen IMDB-APIa, ja palauttaa tulokset listassa

        Args:
            searchword: hakusana
        """

        if len(searchword) == 0:
            self.movie_list = []
            return self.movie_list
        response = requests.get(self.search_url + searchword)
        search_result = response.json()
        results = search_result["results"]
        self.result_length = len(results)
        self.movie_list = []
        for i in range(self.result_length):
            self.movie_list.append(SearchMovie(results[i]))
        return self.movie_list

    def request_title(self, title: str):
        """Hakee valitun elokuvan tiedot ja lisää elokuvan tietokantaan
        
        Args:
            title: elokuvan IMDB-nimi
        """

        response = requests.get(self.title_url + title)
        result = response.json()
        movie_item = MovieDetails(result)
        database = DatabaseActions()
        database.select_movies()
        return database.add_movie_to_database(movie_item)
