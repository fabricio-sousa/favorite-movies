import webbrowser

class Movie():
    '''This class stores movie info.'''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year_released, movie_rating):
        '''This is the Self init constructor, containing the following inputs:
           movie_title, movie_storyline, poster_image, trailer_youtube, year_released and movie_rating'''

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year_released
        self.rating = movie_rating

    def show_trailer(self):
        '''This function allows the built-in Python method to open
           a new browser window to play the youtube trailer'''

        webbrowser.open(self.trailer_youtube_url)
