import requests
import json
from search_movie import SearchMovie

class IMDBSearch:

    def __init__(self):
        self.url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"

    def request_search(self, searchword: str):
        response = requests.get(self.url + searchword)
        search_result = response.json()    
        self.results = search_result["results"]
        n = len(self.results)
        print(f"Movies found: {n}")
        self.movie_list = []
        for i in range(n):
            self.movie_list.append(SearchMovie(self.results[i], i + 1))
    
    def select_movie(self):
        for i in self.movie_list:
            print(i.index, i.title, i.release_date)
        movie_selection = int(input("Which movie do you want to add? Press 0 if you don't want to add anything.\n"))
        if movie_selection == 0:
            return
        elif movie_selection > len(self.movie_list):
            print("No such movie is found on the list")
        else:
            print("Movie selected: ")
            print(self.movie_list[movie_selection - 1].title, self.movie_list[movie_selection - 1].release_date)
            



if __name__ == "__main__":
    search = IMDBSearch()
    movie_name = input("Search: ")
    if len(movie_name) >1:
        search.request_search(movie_name)   
    search.select_movie()
