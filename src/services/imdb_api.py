import requests
import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)
from entities.movie_items import SearchMovie, MovieDetails
from database_connection import get_connection

# Luokka on vastuussa api-kutsuista. Tällä hetkellä ainoa api-kutsu on imdb-apin SearchMovie, joka palauttaa sopivat elokuvat.
# Sovelluslogiikkaassa on tällä hetkellä sekaisin myös käyttöliittymän toiminnallisuutta. Ne lähtevät asap pois, kunhan saan guin käyntiin.
#

class IMDBSearch:

    def __init__(self):
        self.search_url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"
        self.title_url = "https://imdb-api.com/en/API/Title/k_grjsr7l7/"
        self.n = 0
    
    # Metodi request_search() saa parametriksi hakusanan, jonka perusteella tehdään api-kutsu. Se dekoodataan käyttämällä Response.json(),
    # jolloin siitä tulee dict. SearchMovie on elokuvaluokka, jolla on konstruktoreina elokuvan tietoja. Näistä muodostetaan uusi lista self.movie_list
    # Jos kaikki onnistui hyvin, palautetaan totuusarvo True ja False jos jossain meni jokin vialle.

    
    def request_search(self, searchword: str):
        if len(searchword) == 0:
            return []
        response = requests.get(self.search_url + searchword)
        search_result = response.json()    
        results = search_result["results"]
        self.n = len(results)
        self.movie_list = []
        for i in range(self.n):
            self.movie_list.append(SearchMovie(results[i]))
        return self.movie_list

    def request_title(self, title: str):
        response = requests.get(self.title_url + title)
        result = response.json()
        movie_item = MovieDetails(result)
        self.add_movie_to_database(movie_item)
    
    #Lisää valitun elokuvan tietokantaan.
    
    def add_movie_to_database(self, selected_movie):
        conn = get_connection()
        conn.execute("INSERT INTO Movies (title, poster, imdb_id, release_date, director, avg_rating, length, length_mins) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [selected_movie.title, 
            selected_movie.poster, 
            selected_movie.id, 
            selected_movie.release_date, 
            selected_movie.director,
            selected_movie.avg_rating,
            selected_movie.length,
            selected_movie.length_mins
            ])            

