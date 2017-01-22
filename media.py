import webbrowser
import urllib
import json


class Movie():
    """
    This is the Movie Datastructure Class.
    Objects of this type contain the following information:
        Attributes:
            title (str): This is the title of the movie
            storyline (str): This is the storyline of the movie
            poster_image_url (str): URL to poster image
            trailer_youtube_url (str): URL to Youtube trailer

    """
    # Constructor to Movie Class
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        youtube_url):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# This creates a Movie object from inputing a title and youtube_url.
# If no movie is found by the title the method will return 0 and
# print a 'Title' not found
def create_movie(title, youtube_url):

    # Using ombdapi to get a json formated
    request_to_ombd_api = urllib.urlopen(
        "http://www.omdbapi.com/?t=" + title + "&y=&plot=short&r=json")
    json_parsed = json.load(request_to_ombd_api)

    # Takes Parsed JSON object and puts it into a Movie Object
    # if the movie exists
    if json_parsed['Response'] == 'False':
        print title+' '+'not found'
        return 0
    else: # Save information into Movie object
        movie = Movie(
            json_parsed['Title'],
            json_parsed['Plot'],
            json_parsed['Poster'],
            youtube_url)
        return movie


