import webbrowser
#Calls the built in web browser

class Movie():
    """Class that stores information related to the class Movie"""

    def __init__(self, movie_title, movie_storyline, movie_release_date,
                 poster_image, trailer_youtube):
        """Initialises the instance variables that are created

        Arguments:
        title = string of movie title
        storyline = string explaining what movie is about
        release_date = string to store movie release_date
        poster_image = string with a url containing a poster image
        trailer_youtube = string with a url containing the movie trailer
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """Allows trailer to open in a webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
