import requests
from search_movie import SearchMovie
from database_test import DatabaseConnection

# Luokka on vastuussa api-kutsuista. Tällä hetkellä ainoa api-kutsu on imdb-apin SearchMovie, joka palauttaa sopivat elokuvat.
# Sovelluslogiikkaassa on tällä hetkellä sekaisin myös käyttöliittymän toiminnallisuutta. Ne lähtevät asap pois, kunhan saan guin käyntiin.
#

class IMDBSearch:

    def __init__(self):
        self.url = "https://imdb-api.com/en/API/SearchMovie/k_grjsr7l7/"
    
    # Metodi request_search() saa parametriksi hakusanan, jonka perusteella tehdään api-kutsu. Se dekoodataan käyttämällä Response.json(),
    # jolloin siitä tulee dict. SearchMovie on elokuvaluokka, jolla on konstruktoreina elokuvan tietoja. Näistä muodostetaan uusi lista self.movie_list
    # Jos kaikki onnistui hyvin, palautetaan totuusarvo True ja False jos jossain meni jokin vialle.

    
    def request_search(self, searchword: str):
        if len(searchword) == 0:
            return False
        response = requests.get(self.url + searchword)
        search_result = response.json()    
        results = search_result["results"]
        self.n = len(results)
        print(f"Movies found: {self.n}")
        self.movie_list = []
        for i in range(self.n):
            self.movie_list.append(SearchMovie(results[i], i + 1))
        if self.n > 0:
            return True
        else:
            return False
    
    #Osittain käyttöliittymämetodi, joka on vastuussa oikean elokuvan valitsemisesta. Elokuva valitaan käyttämällä listan movie_list indeksejä
    #Jos elokuva valitaan, kutsutaan metodia add_movie_to_database
    
    def select_movie(self):
        for i in self.movie_list:
            print(i.index, i.title, i.release_date)
        movie_selection = int(input("Add a movie by pressing the appropriate number. Press 0 if you don't want to add anything.\n"))
        if movie_selection == 0:
            return
        elif movie_selection > self.n:
            print("No such movie is found on the list")
            return
        else:
            print("Movie added: ")
            print(self.movie_list[movie_selection - 1].title, self.movie_list[movie_selection - 1].release_date)
            self.add_movie_to_database(self.movie_list[movie_selection - 1])
    
    #Lisää valitun elokuvan tietokantaan.
    
    def add_movie_to_database(self, selected_movie):
        connection = DatabaseConnection()
        connection.conn.execute("INSERT INTO Movies (title, poster, imdb_id, release_date) \
            VALUES (?, ?, ?, ?)", [selected_movie.title, selected_movie.poster, selected_movie.id, selected_movie.release_date])            

#Tämän osan testaukseen. Sama rakenne kuin movie_application.py. 
if __name__ == "__main__":
    search = IMDBSearch()
    while True:
        searchword = input("Search movie title: ")
        if search.request_search(searchword):
            search.select_movie()
            break
        else:
            print("Error when making search")
