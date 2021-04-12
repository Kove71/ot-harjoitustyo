from imdb_request import IMDBSearch
from database_test import DatabaseConnection

def main():
    connection = DatabaseConnection()
    connection.create_table()
    while True:
        search = IMDBSearch()
        movie_name = input("Search: ")
        search.request_search(movie_name)   
        search.select_movie()
        another_search = int(input("Press 1 if you want to do a new search or press 0 if you want terminate the program. \n"))
        if another_search == 0:
            break
        elif another_search == 1:
            continue

if __name__ == "__main__":
    main()