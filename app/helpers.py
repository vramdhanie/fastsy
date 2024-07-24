from app.authors import AUTHORS
from schemas.book import AuthorCreate, Author


def createAuthor(author: AuthorCreate) -> dict:
    existing = [A for A in AUTHORS if A.first_name ==
                author.first_name and A.last_name == author.last_name]
    if existing:
        return existing[0].dict()
    author_id = len(AUTHORS) + 1
    new_author = Author(id=author_id, **author.dict())
    AUTHORS.append(new_author)
    return new_author.dict()
