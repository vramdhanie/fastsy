from dal.base import DALBase
from models.author import Author
from schemas.author import AuthorCreate, AuthorUpdate


class DALAuthor(DALBase[Author, AuthorCreate, AuthorUpdate]):
    pass


author = DALAuthor(Author)
