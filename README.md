# Favorite Movie Site Creator
This python script creates an movie listing website that has a tile for
each movie you supply it. The tile has an image and the storyline of the
movie. You can also click on the tile if you want to view a trailer of the movie.

## How to use the Movie Site Creator
Make sure that you have Python installed.
  * This was tested with Python 2.7 and have not with 3

Import the Movie Site Creator files
```python
import media
import fresh_tomatoes
```
Use `create_movie(movie_title,trailer_url)` method to create your favorite
 movie objects.
An example of this is shown below:
```python
pulp_fiction = media.create_movie(
          "Pulp Fiction",
          "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
```
An example of referencing the object is below:
```python
your_movie.title
your_movie.storyline
your_movie.poster_image_url
your_movie.trailer_youtube_url
```
Put your favorite movies in a list like the example below
```python
favorite_movies = [pulp_fiction, up, war_dogs, starsky_and_hutch]
```
Now call `fresh_tomatoes.open_movies_page(favorite_movies)`

Your favorite movies should pop open on your default browser.

You can run this example with example.py

## Known Issues
The create_movie method requires the youtube url. I haven't found
a reliable way of getting the accurate youtube URL. A possible
way could be using the youtube API.



