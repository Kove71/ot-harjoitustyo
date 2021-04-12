import requests
from search_movie import SearchMovie
from database_test import DatabaseConnection

class IMDBSearch:

    def __init__(self):
        self.url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"

    def request_search(self, searchword: str):
        response = requests.get(self.url + searchword)
        search_result = response.json()    
        results = search_result["results"]
        self.n = len(results)
        print(f"Movies found: {self.n}")
        self.movie_list = []
        for i in range(self.n):
            self.movie_list.append(SearchMovie(results[i], i + 1))
    
    def select_movie(self):
        for i in self.movie_list:
            print(i.index, i.title, i.release_date)
        movie_selection = int(input("Which movie do you want to add? Press 0 if you don't want to add anything.\n"))
        if movie_selection == 0:
            return
        elif movie_selection > self.n:
            print("No such movie is found on the list")
            return
        else:
            print("Movie added: ")
            print(self.movie_list[movie_selection - 1].title, self.movie_list[movie_selection - 1].release_date)
            self.add_movie_to_database(self.movie_list[movie_selection - 1])
    
    def add_movie_to_database(self, selected_movie):
        connection = DatabaseConnection()
        connection.conn.execute("INSERT INTO Movies (title, poster, imdb_id, release_date) \
            VALUES (?, ?, ?, ?)", [selected_movie.title, selected_movie.poster, selected_movie.id, selected_movie.release_date])            


if __name__ == "__main__":
    search = IMDBSearch()
    movie_name = input("Search: ")
    search.request_search(movie_name)   
    search.select_movie()

