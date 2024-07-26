from app.dal.base import DALBase
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class DALBook(DALBase[Book, BookCreate, BookUpdate]):
    ...


book = DALBook(Book)
