from sqlalchemy import Column, Integer, String
from app.db import Base


class Movie(Base):
    __tablename__ = "movies"
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String, nullable=False)