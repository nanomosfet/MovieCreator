# Favorite Movie Site Creator
This python script creates an movie listing website that has a tile for
each movie you supply it. The tile has an image and the storyline of the
movie. You can also click on the tile if you want to view a trailer of the movie.

## How to use the Movie Site Creator
1. Make sure that you have Python installed.
  * This was tested with Python 2.7 and have not with 3
2. Create a new python script
3. Import the Movie Site Creator files
```python
import media
import fresh_tomatoes
```
4. Use `create_movie(movie_title,trailer_url)` method to create your favorite
 movie Objects.
  *an example of this is shown below:
  ```python
  pulp_fiction = media.create_movie(
            "Pulp Fiction",
            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
  ```
  *This creates a Movie object which contains the following information
    *Title
    *Poster URL
    *Youtube Trailer URL
    *Movie Story line
  An example of referencing them is below:
  ```python
  your_movie.title
  your_movie.storyline
  your_movie.poster_image_url
  your_movie.trailer_youtube_url
  ```
5. Put your favorite movies in a list like the example below
```python
favorite_movies = [pulp_fiction, up, war_dogs, starsky_and_hutch]
```
6. Now call `fresh_tomatoes.open_movies_page(favorite_movies)`

Now your favorite movies should pop open on your default browser!



