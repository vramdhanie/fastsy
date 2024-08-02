from app.dal.base import DALBase
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorUpdate


class DALAuthor(DALBase[Author, AuthorCreate, AuthorUpdate]):
    pass


author = DALAuthor(Author)
