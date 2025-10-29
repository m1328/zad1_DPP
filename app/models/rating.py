from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db import Base


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True, nullable=False)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True, nullable=False)
    rating = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)