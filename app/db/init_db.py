import logging
from sqlalchemy.orm import Session
from authors import AUTHORS
from books import BOOKS
import dal
import schemas

logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    for author in AUTHORS:
        dal.author.create(db, obj_in=author)

    for book in BOOKS:
        dal.book.create(db, obj_in=book)
