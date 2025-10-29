from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True, nullable=False)
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True, nullable=False)
    tag = Column(String, nullable=False)
    timestamp = Column(Integer, nullable=False)
