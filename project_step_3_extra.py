# Your New Tasks
# Refactor Using Functions: Organize your code by encapsulating the search logic within a function named search.

# This will make your code cleaner, more modular, and easier to maintain.
# Implement Caching: To improve the search speed on future runs, integrate caching into your search function.

# Caching temporarily stores results of operations, so when the same search query is made again, results can be returned instantly without re-processing.
# To get started with caching in Python, read more about caching in Python here.
# Fuzzy Search Logic: Enhance the search functionality to handle typos or spelling mistakes in search queries, allowing it to return relevant results even
# when the search terms are not perfectly matched.

# There are python libraries that help you find close matches to a given search term.
# A useful starting point is the fuzzywuzzy library, which you can learn more about here.
# Example useage (for fuzzy search)
# This is how a fuzzy search should look like to the user:

# Enter your search terms: dirctor:"Stven Spilberg" genre:Advnture

# Results:
# Raiders of the Lost Ark, Director: Steven Spielberg, Year: 1981, Genre: Adventure, Action
# Jurassic Park, Director: Steven Spielberg, Year: 1993, Genre: Adventure, Sci-Fi
# Note how the relevant results were returned, even though there were typos in the input

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# def search():

import csv    
import re

'''
NOTETOSELF:
movies.csv contains repeated movies and information about them. Hence output may not be as desired

edit: modified to show non duplicated results

NOTETOSELF:
output is not exactly the same as shown in expected output, as the movie "Raiders of the Lost Ark" is not included in movies.csv.
'''

csv_file_path = input("Add file path: ")
search_query = input("Enter your search terms: ")

def csv_dict():
    with open(csv_file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        lines = list(csv_reader)
    return lines

def expected_values():
    lines = csv_dict()
    # sets are used to prevent duplicates
    title_expected_values = set()
    director_expected_values = set()
    genre_expected_values = set()
    year_expected_values = set()

    for movie_dictionary in lines:
        for key,value in movie_dictionary.items():
            match key:
                case "title":
                    title_expected_values.add(value)
                case "director":
                    if "|" in value: # | means 2 or more 
                        separated_dir = [d.strip() for d in value.split("|")] 
                        director_expected_values.update(separated_dir)
                    else: 
                        director_expected_values.add(value.strip())
                case "genre":
                    if "|" in value: # | means 2 or more 
                        separated_genre = [g.strip() for g in value.split("|")]
                        genre_expected_values.update(separated_genre)
                    else: 
                        genre_expected_values.add(value.strip())
                case "year":
                    year_expected_values.add(value)

    # return a dictionary as result 
    return {
        "title": list(title_expected_values),
        "director": list(director_expected_values),
        "genre": list(genre_expected_values),
        "year": list(year_expected_values)
    }

def parse_search_terms(search_query):
    # Regular expression to find field:value patterns, considering quotes
    pattern = re.compile(r'(\w+):"([^"]+)"|(\w+):(\S+)')
    matches = pattern.findall(search_query)
    
    # list of expected_fields
    expected_fields = ["title", "director", "genre", "year"]

    # dictionary of expected values for each field
    expected_values_dict = expected_values() 

    search_terms = {}
    for match in matches:
        raw_field = match[0] or match[2]
        raw_value = match[1] or match[3]

        # correct field name using fuzzy match
        corrected_field = process.extractOne(raw_field, expected_fields, score_cutoff=70)

        if corrected_field:
            field = corrected_field[0]

            if field in expected_values_dict:
                corrected_value = process.extractOne(raw_value, expected_values_dict[field], score_cutoff=75)
    
                if corrected_value:
                    value = corrected_value[0]
                else:
                    value = raw_value
            
            else:
                value = raw_value # keep original if field has no expected values

        else:
            field = raw_field
            value = raw_value

        search_terms[field] = value
    return search_terms

def load_movies(csv_file_path):
    search_terms = parse_search_terms(search_query) 
    lines = csv_dict()

    # Initialize search result list with scores
    search_results = []

    # Search for matching movies and calculate scores
    for movie in lines:
        score = 0
        match_count = 0  
        for field, value in search_terms.items():
            if field in movie: #field eg. ('Adventure', 94)
                movie_value = movie[field]
                if field == 'genre':
                    if value in movie_value: # in <string>' requires string as left operand, not tuple. Currently a tuple instead of a dictionary
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
    

load_movies(csv_file_path)

# dirctor:"Stven Spilberg" genre:Advnture