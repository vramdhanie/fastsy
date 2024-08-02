from sqlalchemy import Column, Table, Integer, ForeignKey
from app.db.base import Base

book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.id"), primary_key=True),
)
