from app.dal.base import DALBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class DALUser(DALBase[User, UserCreate, UserUpdate]):
    pass


user = DALUser(User)
