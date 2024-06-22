# Project Step 1
# Jetflix are pleased with your work so far, but they required more features.

# The current search feature is limited, only allowing users to search using a single term and being case-sensitive.

# Your goal is to enhance this feature to make it more flexible and user-friendly.

# Bouns tasks
# Multiple Search Terms: The enhanced search feature should allow users to input more than one search term.
# This means if a user inputs multiple terms, the search should return results relevant to any of those terms.
# For example, if the user searches for "lion king", the system should look for records containing "lion" or "king" (or both).
# Case Insensitive Search: Implement case insensitive search.
# Case insensitive means that search results are the same regardless of whether the search terms are in uppercase, lowercase, or a mix of both.
# For example, searching for "Matrix", "matrix", or "MATRIX" should yield the same results.
# Recall the Last Search and Result: Add functionality to recall the last search query and its result.
# If the user inputs the keyword "last", the application should display the last search they performed and the result of that search.
# For example, if the user's last search was "harry potter" and it returned three results, inputting "last" should display the search 
# term "harry potter" along with a summary of the three articles found.



movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]
identified_movie_titles = []

while True: 
    search = input("Enter search terms (type 'last' to recall last search): ")
    if search.lower() == "last":
        if identified_movie_titles:
            print(f"Last search: {", ".join(identified_movie_titles)}")
        else:
            print("No previous last search found. Start a new search?")
        continue # prompt for new search

    search_terms = search.split(" ")
    identified_movie_titles.clear()

    for movie_title in movies:
        for search_term in search_terms:
            if search_term.lower() in movie_title.lower() and movie_title not in identified_movie_titles:
                identified_movie_titles.append(movie_title)
    
    # since search engine should always be running, I did not include a break

    print(identified_movie_titles)