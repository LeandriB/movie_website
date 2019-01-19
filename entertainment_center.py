import fresh_tomatoes
import media

"""Created instances of favorite movies, each with it's own
   information that is unique to that movie. By creating
   these instances the __init__ function gets called through
   the class Movie."""

a_quiet_place = media.Movie("A Quiet Place",
                            "A family is forced to live in silence while hiding from monster with sensitive hearing",
                            "2018",
                            "https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=WR7cc5t7tv8")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                                    "Avengers reunite to battle their most powerful enemy yet - Thanos",
                                    "2018",
                                    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

deadpool = media.Movie("Deadpool",
                       "A former mercenary operative with a morbid sense of humor is subjected to an experiment that leaves him with healing powers and a quest for revenge",
                       "2016",
                       "https://i.pinimg.com/originals/1a/70/6e/1a706e0021180f77cf766c219319045f.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA&t=59s")

harry_potter_6 = media.Movie("Harry Potter and The Half Blood Prince",
                             "Harry attends Hogwarts for his 6th year and learns more about Voldermort's dark past",
                             "2009",
                             "https://cdn.shopify.com/s/files/1/1402/3931/products/harry6.jpg?v=1481264710",
                             "https://www.youtube.com/watch?v=tAiy66Xrsz4")


inception = media.Movie("Inception",
                        "A thief with the ability to enter people's dreams and steal secrets from their subconscious",
                        "2010",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=Qwe6qXFTdgc")

ready_player_one = media.Movie("Ready Player One",
                               "In the year 2045, people can escape their everyday life by immersing themselves in a virtual world",
                               "2018",
                               "https://cdn.images.express.co.uk/img/dynamic/36/590x/secondary/ready-player-one-poster-1157633.jpg",
                               "https://www.youtube.com/watch?v=cSp1dM2Vj48")

movies = [a_quiet_place, avengers_infinity_war, deadpool,
          harry_potter_6, inception, ready_player_one]
          #Array with list of favorite movies

fresh_tomatoes.open_movies_page(movies)
#Opens web page that displays the list of movies in the array
