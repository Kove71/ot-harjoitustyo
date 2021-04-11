import requests
import json

class IMDB_search:

    def __init__(self):
        self.url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"

    def request_search(self, searchword: str):
        response = requests.get(self.url + searchword)
        self.search_result = response.json()    
        self.results = self.search_result["results"]
        self.movie = self.results[0]
    
    def movie_details(self):
        print(self.movie["title"], self.movie["description"])



if __name__ == "__main__":
    search = IMDB_search()
    movie_name = input("Search: ")
    if len(movie_name) >1:
        search.request_search(movie_name)   
    search.movie_details() 
    
