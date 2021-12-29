import requests

API_KEY = "200a31808b3f8645cbb7354128260a92"
IMAGE_URL = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2"


def convert_data(movie_data):
    movie_data.update({
        "tmdb_id": movie_data["id"],
        "poster_image": IMAGE_URL + movie_data["poster_path"] if movie_data["poster_path"] else "",
        "original_language_iso": movie_data["original_language"]
    })


def get_url(movie_id):
    return "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id, API_KEY)


def parse(movie_id):
    response = requests.get(get_url(movie_id))
    if response.status_code == 200:
        movie_data = response.json()
        convert_data(movie_data)
        print(movie_data)
        r = requests.post("http://127.0.0.1:8000/movies/create/", json=movie_data)
        print(movie_id, r.json())


if __name__ == "__main__":
    for i in range(1, 200):
        parse(i)
