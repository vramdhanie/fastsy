from dal.base import DALBase
from models.book import Book
from schemas.book import BookCreate, BookUpdate


class DALBook(DALBase[Book, BookCreate, BookUpdate]):
    ...


book = DALBook(Book)
