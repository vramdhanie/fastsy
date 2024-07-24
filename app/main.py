from fastapi import FastAPI, APIRouter, Request
from typing import Optional
from schemas.book import Book, BookCreate
from app.books import BOOKS
from app.authors import AUTHORS
from app.helpers import createAuthor
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=BASE_PATH / "templates")

api = FastAPI(title="Fast SY")
router = APIRouter()


@router.get("/", status_code=200)
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "books": BOOKS})


@router.get("/book/search", status_code=200, response_model=Book)
def search_book(q: Optional[str] = None, max: Optional[int] = 10) -> dict:
    result = [B for B in BOOKS if q and q.lower() in B.title.lower()]
    return {"q": q, "max": max, "results": result[:max]}


@router.get("/book/{book_id}", status_code=200)
def get_book(book_id: int) -> dict:
    result = [B for B in BOOKS if B.id == book_id]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Book with id {book_id} not found")
    return result[0]


@router.post("/book", status_code=201, response_model=Book)
def create_book(book: BookCreate) -> dict:
    new_authors = [createAuthor(A) for A in book.authors]
    book_id = len(BOOKS) + 1
    book = Book(id=book_id,  authors=new_authors, title=book.title,
                year=book.year, description=book.description)
    BOOKS.append(book)
    return book


@router.get("/author/{author_id}", status_code=200)
def get_author(author_id: int) -> dict:
    result = [A for A in AUTHORS if A.id == author_id]
    return result[0].dict() if result else {}


@router.get("/author/search", status_code=200)
def search_author(q: Optional[str] = None, max: Optional[int] = 10) -> dict:
    result = [A for A in AUTHORS if q and q.lower() in A.first_name.lower()
              or q.lower() in A.last_name.lower()]
    return {"q": q, "max": max, "results": result[:max]}


api.include_router(router, prefix="/api")
