from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List
from .author import Author
from .book_author import book_author


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), index=True, nullable=False)
    year = Column(Integer, index=True, nullable=False)
    description = Column(String(1024), nullable=True)
    authors: Mapped[List[Author]] = relationship(
        "Author", secondary=book_author, back_populates="books")
