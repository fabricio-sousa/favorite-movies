import media
import fresh_tomatoes

'''Individual instances of the class Movie are created'''

dracula = media.Movie("Dracula",
                        "The story of Count Dracula as told by Bram Stoker.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Bram_Stoker%27s_Draula_%281992_film%29.jpg",
                        "https://www.youtube.com/watch?v=PlDbxogHPao",
                        "1992",
                        "Rated R")

interview_with_the_vampire = media.Movie("Interview with the Vampire",
                     "A tale of two vampires and their daughter.",
                     "https://upload.wikimedia.org/wikipedia/en/f/fe/InterviewwithaVampireMoviePoste.JPG",
                     "https://www.youtube.com/watch?v=qmFYu8x46VY",
                     "1994",
                     "Rated R")

wonder_woman = media.Movie("Wonder Woman",
                           "The origin story of the most bad ass heroine ever.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
                           "2017",
                           "Rated PG-13")



the_name_of_the_rose = media.Movie("The Name of the Rose",
                           "A medieval murder mystery in a monastery of Franciscan monks.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c4/Name_of_rose_movieposter.jpg",
                           "https://www.youtube.com/watch?v=7-yYJgpQ-CE",
                           "1986",
                           "Rated R")

et = media.Movie("E.T.",
                           "A friendly alien visits planet Earth.",
                           "https://upload.wikimedia.org/wikipedia/en/6/66/E_t_the_extra_terrestrial_ver3.jpg",
                           "https://www.youtube.com/watch?v=qYAETtIIClk",
                           "1982",
                           "Rated PG")

close_encounters = media.Movie("Close Encounters of the Third Kind",
                           "Humanity makes direct contact with an alien species.",
                           "https://upload.wikimedia.org/wikipedia/en/b/ba/Close_Encounters_of_the_Third_Kind_%281977%29_theatrical_poster.jpg",
                           "https://www.youtube.com/watch?v=dSpQ3G08k48",
                           "1977",
                           "Rated PG")

'''A list movies is created with the 6 individual movie instances'''
movies = [dracula, interview_with_the_vampire, wonder_woman, the_name_of_the_rose, et, close_encounters]

'''The movie website is generated'''
fresh_tomatoes.open_movies_page(movies)
