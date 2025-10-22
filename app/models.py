from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .db import Base


class Movie(Base):
    __tablename__ = "movies"
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String, nullable=False)


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True)
    imdbId = Column(String)
    tmdbId = Column(String)


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True, nullable=False)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True, nullable=False)
    rating = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True, nullable=False)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True, nullable=False)
    tag = Column(String, nullable=False)
    timestamp = Column(Integer, nullable=False)
