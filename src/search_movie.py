class SearchMovie:

    def __init__(self, movie: dict, index: int):
        self.movie = movie
        self.title = self.movie["title"]
        self.release_date = self.movie["description"]
        self.poster = self.movie["image"]
        self.id = self.movie["id"]
        self.index = index