# Project Step 2 Extra
# Searching by one field is nice, but it's not enough.

# Users have requested the feature of searching by multiple fields.

# For example: Searching for action movies from 1985 by James Cameron.

# Your task
# Allow users to combine multiple search fields (e.g., director, year, genre) and terms in their queries.
# For example, a user should be able to search for all "Sci-Fi" movies released in "1999", or find all movies directed by "Steven Spielberg" 
# in the "Adventure" genre.
# The search fields will be integrated into your search query, using the syntax field:value.
# Allow the user to use quotes (" ") for values with a space in them.
# For example, the user can search for director:"James Cameron" genre:Drama year:1985
# Think of a way to rank and sort your results.
# Movies that match more search criteria should be ranked higher in the search results.
# For example, if a user searches for "Action" movies from "1985" directed by "James Cameron", a movie that matches all three criteria should 
# appear before movies that match only one or two.
# Example usage
# Enter your search terms: director:"Robert Zemeckis" genre:Drama year:1994

# Results:
# Forrest Gump, Director: Robert Zemeckis, Year: 1994, Genre: Drama, Romance
# The Shawshank Redemption, Director: Frank Darabont, Year: 1994, Genre: Drama
# The Lion King, Director: Roger Allers, Rob Minkoff, Year: 1994, Genre: Animation, Adventure, Drama

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

import re
search = input("Enter your search terms: ")


def parse_search_terms(search):
    # Regular expression to find field:value patterns, considering quotes
    pattern = re.compile(r'(\w+):"([^"]+)"|(\w+):(\S+)')
    matches = pattern.findall(search)

    search_terms = {}
    for match in matches:
        field = match[0] or match[2]
        value = match[1] or match[3]
        search_terms[field] = value

    return search_terms

search_terms = parse_search_terms(search) # dictioanry

# Initialize search result list with scores
search_results = []

# Search for matching movies and calculate scores
for movie in movies:
    score = 0
    match_count = 0  
    for field, value in search_terms.items():
        if field in movie:
            movie_value = movie[field]
            if field == 'genre':
                if value in movie_value:
                    match_count += 1
            elif field == 'year':
                if str(movie_value) == value:
                    match_count += 1
            elif field == 'title':
                if str(movie_value) == value:
                    match_count += 1
            elif field == 'director':
                if str(movie_value) == value:
                    match_count += 1

    score = match_count
    if score > 0:  # Only include movies with at least one match
        search_results.append([score, movie])

final_list = []

for i in range(1,len(search_terms)+1):
    for search_res in search_results:
        match_count = search_res[0]
        if match_count == i:
            final_list.append(search_res)

final_list = final_list[::-1]
for movie in final_list:
    match = movie[0]
    movie_dictionary = movie[1]
    title = movie_dictionary['title']
    director = movie_dictionary["director"]
    year = movie_dictionary['year']
    genre = movie_dictionary['genre']

    print(f"(Match: {match}/{len(search_terms)})  Movie name: {title}, directed by: {director}. Year: {year:}. Genre: {genre}")

# director:"Robert Zemeckis" genre:Drama year:1994