# Your task
# Add to your project a function called "load_movies".

# The function will receive the file path as input.
# It will return a list of the movies properties represented as dictionaries.
# Example
# # example call to your function
# >>> movies = load_movies("C:\\Temp\\movies.csv")
# >>> print(movies)
# [
#     {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "genre": "Drama"},
#     {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "genre": "Crime, Drama"},
#     {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action, Crime, Drama"},
#     ...
# ]
# Use project_step_3.py as a starting point.

# Use the csv module to read the file.

# It has a special feature called a DictReader - which is used to read CSV data into Python dictionaries.

# This is an example how to use the csv module to read a file:

# import csv

# # Specify the path to your CSV file
# csv_file_path = 'path/to/your/file.csv'

# # Open the CSV file for reading
# with open(csv_file_path, 'r') as file:
#     # Create a CSV reader
#     csv_reader = csv.DictReader(file)
#     # Get all of the lines in the CSV file
#     lines = []
#     for line in csv_reader:
#         print(line)
#         lines.append(line)

import csv    
import re

'''

NOTETOSELF:
movies.csv contains repeated movies and information about them. Hence output may not be as desired

edit: modified line 101 to show non duplicated results
'''


csv_file_path = input("Add file path: ")
with open(csv_file_path, "r") as file:
    csv_reader = csv.DictReader(file)
    lines = []

    for line in csv_reader: # make a list of dictionaries
        lines.append(line)

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

def load_movies(csv_file_path):
    search_terms = parse_search_terms(search) 

    # Initialize search result list with scores
    search_results = []

    # Search for matching movies and calculate scores
    for movie in lines:
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
        if score > 0 and [score,movie] not in search_results:  # Only include movies with at least one match + check if list in search_results since movies.csv has duplicates
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

load_movies(csv_file_path)
