from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.book_author import book_author
from typing import List, Mapped
from app.models.book import Book


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(128), index=True, nullable=False)
    last_name = Column(String(128), index=True, nullable=False)
    books: Mapped[List[Book]] = relationship("Book", secondary=book_author,
                                             back_populates="authors")
