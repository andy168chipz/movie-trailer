import media
import fresh_tomatoes

# creat movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",# NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_prestige = media.Movie("The Prestige",
                           "Are you watching closely?",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg", # NOQA
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI")

lord_of_the_rings = media.Movie("LOTR:Return of the Kings",
                                 "Epic travels",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg", # NOQA
                                 "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

inception = media.Movie("Inception",
                        "Is it a dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # NOQA
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

# list of movie objects
movies = [toy_story, avatar, the_prestige, lord_of_the_rings, inception]

# creates the webpage using the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
