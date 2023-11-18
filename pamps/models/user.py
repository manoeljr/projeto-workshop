from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from pamps.security import HashedPassword

if TYPE_CHECKING:
    from pamps.models.post import Post


class User(SQLModel, table=True):
    """ Represents the User Model """

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    posts: List["Post"] = Relationship(back_populates="user")
