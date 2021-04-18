#Luokka hakutulosten elokuville.

class SearchMovie:

    def __init__(self, movie: dict):
        self.title = movie["title"]
        self.description = movie["description"]
        self.poster = movie["image"]
        self.id = movie["id"]

class MovieDetails:

    def __init__(self, movie: dict):
        self.title = movie["title"]
        self.release_date = movie["releaseDate"]
        self.director = movie["directors"]
        self.avg_rating = movie["imDbRating"]
        self.poster = movie["image"]
        self.length = movie["runtimeStr"]
        self.length_mins = movie["runtimeMins"]
        self.id = movie["id"]
