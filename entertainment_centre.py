import media  # import media file for the class definition
import fresh_tomatoes  # import fresh_tomatoes file for the layout

# create instances of the class Movie
# add info: title, storyline, poster image url and youtube trailer url

interstellar = media.Movie("Interstellar",
                           "In futuristic 21st century, a pilot embarks on "
                           "intergallactic travel to find a new planet for "
                           "mankind to survive",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")
tfios = media.Movie("The Fault in Our Stars",
                    "A motivating story about 2 people who love and live "
                    "life within the numbered days",
                    "https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png",
                    "https://www.youtube.com/watch?v=9ItBvH5J6ss")

harry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
                     "An orphan boy discovers that he is a wizard and "
                     "is invited to study at Hogwarts",
                     "http://assets.flicks.co.nz/images/movies/poster/49/494ba9ff03bdad881378a6fd4092a6c7_500x735.jpg",
                     "https://www.youtube.com/watch?v=PbdM1db3JbY")
titanic = media.Movie("Titanic",
                      "A love story on the ship Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

the_avengers = media.Movie("The Avengers",
                           "A group of superheroes save planet Earth",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")
a_walk_to_remember = media.Movie("A Walk to Remember",
                                 "A dying girl teaches the true meaning of "
                                 "love to a young boy",
                                 "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                                 "https://www.youtube.com/watch?v=k3B2XBcp7vA")

movies_list = [interstellar, tfios, harry_potter, titanic,
               the_avengers, a_walk_to_remember] # make a list of movies

# pass the list of movies to the function open_movies_page for styling
fresh_tomatoes.open_movies_page(movies_list)
