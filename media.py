import webbrowser


class Movie():

    """ This class provides a way to store movie related info

    Example:
        Create a Movie object by giving the movie title, movie storyline,
        poster image url and youtube trailer.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self, movie_title,
            movie_storyline, poster_image,
            trailer_youtube):
        # assignment of instance vars
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # opens the default broswer to the specified youtube trailer url
        webbrowser.open(self.trailer_youtube_url)
