from pydantic import BaseModel


class MovieOut(BaseModel):
    movieId: int
    title: str
    genres: str
    class Config: orm_mode = True


class LinkOut(BaseModel):
    id: int
    movieId: int
    imdbId: str | None = None
    tmdbId: str | None = None
    class Config: orm_mode = True


class RatingOut(BaseModel):
    id: int
    userId: int
    movieId: int
    rating: float
    timestamp: int
    class Config: orm_mode = True


class TagOut(BaseModel):
    id: int
    userId: int
    movieId: int
    tag: str
    timestamp: int
    class Config: orm_mode = True
