import requests
import base


API_KEY = base.API_KEY


def search_movie(movie_name):

    url = "https://www.omdbapi.com/"

    params = {
        "apikey": API_KEY,
        "s": movie_name,
        "type": "movie"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "ERROR"

    else:
        response = response.json()

        if response["Response"] != "True":
            return "ERROR"

        movies = response["Search"]

        return movies[:5]


def get_movie_info(imdb_id):

    url = "https://www.omdbapi.com/"

    params = {
        "apikey": API_KEY,
        "i": imdb_id,
        "plot": "full"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "ERROR"

    else:
        response = response.json()

        if response["Response"] != "True":
            return "ERROR"

        return response


def get_popular_movies():

    popular_movies = [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers",
        "Titanic"
    ]

    movies = []

    for movie_name in popular_movies:

        result = search_movie(movie_name)

        if result != "ERROR":
            movies.append(result[0])

    return movies


if __name__ == "__main__":

    movie_name = input("Enter movie name: ")

    result = search_movie(movie_name)

    print(f"result: {result}")