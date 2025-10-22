import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Movie(BaseModel):
    movieId: int
    title: str
    genres: str


class Link(BaseModel):
    movieId: int
    imdbId: str
    tmdbId: str


class Rating(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

class Tag(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int


movies_df = pd.read_csv("database_files/movies.csv")
links_df = pd.read_csv("database_files/links.csv")
ratings_df = pd.read_csv("database_files/ratings.csv")
tags_df = pd.read_csv("database_files/tags.csv")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/movies", response_model=List[Movie])
def get_movies():
    movies = [Movie(**movie) for _, movie in movies_df.iterrows()]
    return movies


@app.get("/links", response_model=List[Link])
def get_links():
    links = [Link(**link) for _, link in links_df.iterrows()]
    return links


@app.get("/ratings", response_model=List[Rating])
def get_ratings():
    ratings = [Rating(**rating) for _, rating in ratings_df.iterrows()]
    return ratings


@app.get("/tags", response_model=List[Tag])
def get_tags():
    tags = [Tag(**tag) for _, tag in tags_df.iterrows()]
    return tags
