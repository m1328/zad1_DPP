from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import engine, Base, get_db
from . import schemas
from .models import Movie, Link, Rating, Tag

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movies API (SQLite)")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/movies", response_model=list[schemas.MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@app.get("/links", response_model=list[schemas.LinkOut])
def list_links(db: Session = Depends(get_db)):
    return db.query(Link).all()


@app.get("/ratings", response_model=list[schemas.RatingOut])
def list_ratings(db: Session = Depends(get_db)):
    return db.query(Rating).all()


@app.get("/tags", response_model=list[schemas.TagOut])
def list_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()
