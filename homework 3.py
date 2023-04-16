# PPHA 30535
# Spring 2023
# Homework 3

# Tianhua Song

# tianhuas
# SkySong4

# Due date: Sunday April 16th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/rating/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

#from numpy import random

#class MovieDataBase():
#    def __init__(self):
#        self.titles = []
#        self.movies = {}

#    def add_movie(self, title, year, category, rating, num_stars):
#        self.titles.append(title)
#        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
#        print(f'{title} ({year}) added to the database.')

#    def what_to_watch(self):
#        choice = random.choice(self.titles)
#        movie = self.movies[choice]
#        print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, rating, num_stars):
        self.titles.append(title)
        self.movies[title] = {'year': year, 'category': category, 'rating': rating, 'stars': num_stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category=None):
        if not self.titles:
            try:
                raise ValueError("No movies in the database.")
            except ValueError as e:
                print("Error:", e)
                return

        if category:
            titles_by_category = [title for title in self.titles if self.movies[title]['category'] == category]
            if not titles_by_category:
                print(f"No movies found in the '{category}' category.")
                return
            choice = random.choice(titles_by_category)
        else:
            choice = random.choice(self.titles)

        movie = self.movies[choice]
        print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")


class InteractiveMovieDataBase(MovieDataBase):
    def add_movie(self, title=None, year=None, category=None, rating=None, num_stars=None):
        if title is None or year is None or category is None or rating is None or num_stars is None:
            title = input("Enter movie title: ")
            year = input("Enter movie year: ")
            category = input("Enter movie category: ")
            rating = input("Enter movie rating: ")
            num_stars = input("Enter number of stars: ")

            # Check if the inputs are valid
           if not title or not title.strip():
                print("Error: Invalid title. Title should not be empty or None.")
                return

            if not category or not category.strip():
                print("Error: Invalid category. Category should not be empty or None.")
                return

            if not rating or not rating.strip():
                print("Error: Invalid rating. Rating should not be empty or None.")
                return
            
             try:
                year = int(year)
                num_stars = float(num_stars)
            except ValueError:
                print("Error: Invalid input. Year should be an integer and stars should be a number.")
                return

            if not (1 <= num_stars <= 5):
                print("Error: Invalid stars value. It should be between 1 and 5.")
                return

        super().add_movie(title, year, category, rating, num_stars)

    def movie_rankings(self):
        ranked_titles = sorted(self.titles, key=lambda title: self.movies[title]['stars'], reverse=True)
        return ranked_titles



