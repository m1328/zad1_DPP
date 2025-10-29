from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True)
    imdbId = Column(String)
    tmdbId = Column(String)