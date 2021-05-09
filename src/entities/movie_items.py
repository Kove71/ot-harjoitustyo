class SearchMovie:
    """Tietoluokka, jossa on tiedot hakuelokuvista
    """

    def __init__(self, movie: dict):
        """Luokan konstruktori.

        Args:
            movie: dict, joka on purettu apin palauttamasta JSON:sta
        """

        self.title = movie["title"]
        self.description = movie["description"]
        self.poster = movie["image"]
        self.id = movie["id"]

class MovieDetails:
    """Tietoluokka, jossa on tiedot tietokantaan lisättävästä elokuvasta.
    """

    def __init__(self, movie: dict):
        """Luokan konstruktori.

        Args:
            movie: dict, joka on purettu apin palauttamasta JSON:sta
        """

        self.title = movie["title"]
        self.release_date = movie["releaseDate"]
        self.director = movie["directors"]
        self.avg_rating = movie["imDbRating"]
        self.poster = movie["image"]
        self.length = movie["runtimeStr"]
        self.length_mins = movie["runtimeMins"]
        self.id = movie["id"]
