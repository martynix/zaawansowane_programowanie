from fastapi import FastAPI
import pandas as pd

app = FastAPI()


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


@app.get("/movies")
def get_movies():
    df = pd.read_csv("movies.csv")
    movies_list = []

    for index, row in df.iterrows():
        movie_obj = Movie(
            movieId=row["movieId"], title=row["title"], genres=row["genres"]
        )
        movies_list.append(movie_obj.__dict__)
    return movies_list


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


@app.get("/ratings")
def get_ratings():
    df = pd.read_csv("ratings.csv")
    ratings_list = []

    for index, row in df.iterrows():
        rating_obj = Rating(
            userId=row["userId"],
            movieId=row["movieId"],
            rating=row["rating"],
            timestamp=row["timestamp"],
        )
        ratings_list.append(rating_obj.__dict__)
    return ratings_list


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


@app.get("/links")
def get_links():
    df = pd.read_csv("links.csv")
    links_list = []

    for index, row in df.iterrows():
        link_obj = Link(
            movieId=row["movieId"], imdbId=row["imdbId"], tmdbId=row["tmdbId"]
        )
        links_list.append(link_obj.__dict__)
    return links_list


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


@app.get("/tags")
def get_tags():
    df = pd.read_csv("tags.csv")
    tags_list = []

    for index, row in df.iterrows():
        tag_obj = Tag(
            userId=row["userId"],
            movieId=row["movieId"],
            tag=row["tag"],
            timestamp=row["timestamp"],
        )
        tags_list.append(tag_obj.__dict__)
    return tags_list


# pip install fastapi uvicorn
# uvicorn zad_1-4:app --reload
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/ratings
# http://127.0.0.1:8000/links
# http://127.0.0.1:8000/tags
