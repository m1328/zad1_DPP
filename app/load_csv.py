import pandas as pd
from .db import engine, Base, SessionLocal
from . import models


def load_all():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    movies = pd.read_csv("database_files/movies.csv")
    for _, r in movies.iterrows():
        db.add(models.Movie(movieId=int(r.movieId), title=str(r.title), genres=str(r.genres)))

    links = pd.read_csv("database_files/links.csv")
    for _, r in links.iterrows():
        db.add(models.Link(movieId=int(r.movieId),
                           imdbId=None if pd.isna(r.imdbId) else str(r.imdbId),
                           tmdbId=None if pd.isna(r.tmdbId) else str(r.tmdbId)))

    ratings = pd.read_csv("database_files/ratings.csv")
    for _, r in ratings.iterrows():
        db.add(models.Rating(userId=int(r.userId), movieId=int(r.movieId),
                             rating=float(r.rating), timestamp=int(r.timestamp)))

    tags = pd.read_csv("database_files/tags.csv")
    for _, r in tags.iterrows():
        db.add(models.Tag(userId=int(r.userId), movieId=int(r.movieId),
                          tag=str(r.tag), timestamp=int(r.timestamp)))

    db.commit()
    db.close()


if __name__ == "__main__":
    load_all()
