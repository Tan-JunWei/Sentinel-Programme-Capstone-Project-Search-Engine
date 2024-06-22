# Your task
# Modify the search function to allow users to search for movies by specific fields (e.g., director, year). Your code should:

# Let the user to select the field they want to search by, from this list:
# title
# director
# year
# genre
# Search only on this field.
# Example usage:

# Select a search field (title/director/year/genre): genre
# Enter a search term: drama

# Results:
# Forrest Gump, Director: Robert Zemeckis, Year: 1994, Genre: Drama, Romance
# Fight Club, Director: David Fincher, Year: 1999, Genre: Drama
# Empty search field
# Allow the user to leave "search field" empty.
# In this case, search on all fields.
# For example:

# Enter a search field:
# Enter a search term: 2001

# Results:
# Spirited Away, Director: Hayao Miyazaki, Year: 2001, Genre: Animation, Adventure, Family
# 2001: A Space Odyssey, Director: Stanley Kuberick, Year: 1968, Genre: Sci-Fi, Adventure, Drama
# Guidelines
# Your search should be case insensitive.
# Case insensitive means that search results are the same regardless of whether the search terms are in uppercase, lowercase, or a mix of both.
# For example, searching for "Matrix", "matrix", or "MATRIX" should yield the same results.
# Use project_step_2.py as a starting point.

# List of movie titles
movies = [
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "genre": "Drama"},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "genre": "Crime, Drama"},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action, Crime, Drama"},
    {"title": "Forrest Gump", "director": "Robert Zemeckis", "year": 1994, "genre": "Drama, Romance"},
    {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "genre": "Action, Adventure, Sci-Fi"},
    {"title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "year": 1999, "genre": "Action, Sci-Fi"},
    {"title": "Avengers: Infinity War", "director": "Anthony Russo, Joe Russo", "year": 2018, "genre": "Action, Adventure, Sci-Fi"},
    {"title": "Back to the Future", "director": "Robert Zemeckis", "year": 1985, "genre": "Adventure, Comedy, Sci-Fi"},
    {"title": "The Lion King", "director": "Roger Allers, Rob Minkoff", "year": 1994, "genre": "Animation, Adventure, Drama"},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994, "genre": "Crime, Drama"},
    {"title": "Fight Club", "director": "David Fincher", "year": 1999, "genre": "Drama"},
    {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "genre": "Adventure, Drama, Sci-Fi"},
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "year": 2001, "genre": "Animation, Adventure, Family"},
    {"title": "La La Land", "director": "Damien Chazelle", "year": 2016, "genre": "Comedy, Drama, Music"},
    {"title": "Jurassic Park", "director": "Steven Spielberg", "year": 1993, "genre": "Action, Adventure, Sci-Fi"},
    {"title": "Titanic", "director": "James Cameron", "year": 1997, "genre": "Drama, Romance"},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001, "genre": "Adventure, Drama, Fantasy"},
    {"title": "Star Wars: Episode IV - A New Hope", "director": "George Lucas", "year": 1977, "genre": "Action, Adventure, Fantasy"},
    {"title": "Goodfellas", "director": "Martin Scorsese", "year": 1990, "genre": "Biography, Crime, Drama"},
    {"title": "The Silence of the Lambs", "director": "Jonathan Demme", "year": 1991, "genre": "Crime, Drama, Thriller"},
]

field = input("Select a search field (title/director/year/genre): ").lower()
search = input("Enter a search term: ").lower()
years = []

for movie in movies:

    title = movie["title"]
    director = movie["director"]
    year = movie["year"]
    genre = movie["genre"]

    if field:
        # Convert `field` to lower case to handle case insensitivity
        field_lower = field.lower()
        
        # Check if the field exists in the movie dictionary
        if field_lower in movie:
            # Convert the field value to string and search
            if search.lower() in str(movie[field_lower]).lower():
                print(f"{title}, Director: {director}, Year: {year}, Genre: {genre}")
    else:
        # If `field` is empty, search across all fields
        for key, value in movie.items():
            # Convert each value to a string and perform search
            if search.lower() in str(value).lower():
                print(f"{title}, Director: {director}, Year: {year}, Genre: {genre}")
                break
