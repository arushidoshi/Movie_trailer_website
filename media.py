import webbrowser
class Movie():
    """This class defines the structure of storing movie related information"""

    # the init fuction is a constructor
    def __init__(self, movie_title, movie_summary, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_summary
        self.poster = movie_poster
        self.youtube_trailer = movie_trailer

    # to open trailer in a web browser window
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
