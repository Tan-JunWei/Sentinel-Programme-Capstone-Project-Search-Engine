# Project Step 1
# The evil hackers group GrayShadow has destroyed the search function in the popular streaming service Jetflix, and now 
# people can't search their favorite movies and series!

# Let's fix this situation.

# Your task
# First, let's search for movie titles inside a list of movies.

# Write a Python script that:

# Asks the user to input a search term (the name of a movie they're looking for).
# Uses a loop to iterate over the list of movie titles.
# Uses flow control (if statements) to check if the search term exactly matches any of the movie titles in the list.
# Prints the titles that match the search term.
# Prints how many results were found.
# Use project_step_1.py as a starting point.


# Ask the user for a search term

# Search for the movie by iterating over the list

# Print the results
search = input("Enter a search term(the name of a movie you are looking for): ")
# List of movie titles
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]

identified_movie_titles = []

for movie_title in movies:
    if search.lower() in movie_title.lower():
        identified_movie_titles.append(movie_title)

print(f"Titles that match the search term: {", ".join(identified_movie_titles)}")
print(f"Number of search results found: {len(identified_movie_titles)}")
