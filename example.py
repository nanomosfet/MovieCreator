import media
import fresh_tomatoes

# Create movies
pulp_fiction = media.create_movie(
            "Pulp Fiction",
            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

shawshank = media.create_movie(
            "The Shawshank Redemption",
            "https://www.youtube.com/watch?v=6hB3S9bIaco")
up = media.create_movie(
            "Up",
            "https://www.youtube.com/watch?v=pkqzFUhGPJg")

war_dogs = media.create_movie(
            "War Dogs",
            "https://www.youtube.com/watch?v=Rwh9c_E3dJk")
due_date = media.create_movie(
            "Due Date",
            "https://www.youtube.com/watch?v=Hd_aN0LAgMo")

# Put movies into list
favorite_movies = [pulp_fiction, shawshank, up, war_dogs, due_date]

# Open movie site
fresh_tomatoes.open_movies_page(favorite_movies)






