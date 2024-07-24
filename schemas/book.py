from pydantic import BaseModel
from typing import Sequence


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str


class BookBase(BaseModel):
    title: str
    year: int
    description: str


class Book(BaseModel):
    id: int
    title: str
    authors: Sequence[Author]
    year: int
    description: str


class BookSearchResult(BaseModel):
    q: str
    max: int
    results: Sequence[Book]


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str


class BookCreate(BaseModel):
    title: str
    authors: Sequence[AuthorCreate]
    year: int
    description: str
