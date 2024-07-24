from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str


class AuthorDB(BaseModel):
    id: int
    first_name: str
    last_name: str


class Author(AuthorDB):
    pass


class AuthorCreate(AuthorBase):
    pass
