from db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from models.book_author import book_author
from typing import List


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(128), index=True, nullable=False)
    last_name = Column(String(128), index=True, nullable=False)
