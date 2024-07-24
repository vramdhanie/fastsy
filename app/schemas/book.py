from pydantic import BaseModel
from typing import Sequence
from .author import Author, AuthorCreate


class BookBase(BaseModel):
    title: str
    year: int
    description: str
    authors: Sequence[Author]


# Used when submitting a book via POST requests
class BookCreate(BaseModel):
    title: str
    authors: Sequence[AuthorCreate]
    year: int
    description: str

# The book as it Appears in the DB


class BookDB(BaseModel):
    id: int
    title: str
    authors: Sequence[Author]
    year: int
    description: str

    class Config:
        orm_mode = True

# The book as it appears to client


class Book(BookDB):
    pass


class BookSearchResult(BaseModel):
    q: str
    max: int
    results: Sequence[Book]
