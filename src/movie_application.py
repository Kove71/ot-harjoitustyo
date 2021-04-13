from imdb_search import IMDBSearch
from database_test import DatabaseConnection
# Pääohjelma. Kutsuu tietokantaa ja imdb:n hakua. Loopissa on myös alkukantainen tekstikäyttöliittymä, jonka avulla voi testata ohjelman toimivuutta.

def main():
    connection = DatabaseConnection()
    
    # "Alustaa" tietokannan aina kun ohjelma suoritetaan. create_table() tarkistaa jos tietokannassa on jo kyseinen taulukko, ja jos sitä ei löydy, niin taulukko luodaan.
    # Metodia kutsutaan aina kerran ohjelmaa käynnistäessä.
    
    connection.create_table()
    while True:
        search = IMDBSearch()
        while True:
            searchword = input("Search: ")
            if search.request_search(searchword):
                search.select_movie()
                break
            else:
                print("Error when making search")   
        another_search = int(input("Press 1 if you want to do a new search or press 0 if you want terminate the program. \n"))
        if another_search == 0:
            break
        elif another_search == 1:
            continue


if __name__ == "__main__":
    main()