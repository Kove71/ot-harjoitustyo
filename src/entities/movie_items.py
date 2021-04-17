#Luokka hakutulosten elokuville.

class SearchMovie:

    def __init__(self, movie: dict):
        self.movie = movie
        self.title = self.movie["title"]
        self.description = self.movie["description"]
        self.poster = self.movie["image"]
        self.id = self.movie["id"]

class MovieDetails:

    def __init__(self, movie: dict):
        self.movie = movie
        self.title = self.movie["title"]
        self.release_date = self.movie["releaseDate"]
        self.director = self.movie["directors"]
        self.avg_rating = self.movie["imDbRating"]
        self.poster = self.movie["image"]
        self.length = self.movie["runtimeStr"]
        self.length_mins = self.movie["runtimeMins"]
        self.id = self.movie["id"]
        self.review = None
        self.watched = None