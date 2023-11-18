""" Security utilities """
from passlib.context import CryptContext
from pamps.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm


def verify_password(plain_password, hashed_password) -> bool:
    """ Verifies a hash against a password """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """ Generate a hash from plain text """
    return pwd_context.hash(password)


class HashedPassword(str):
    """
        Takes a plain text password and hashes it. Use this as a field in your SQLModel
        Class User(SQLModel, table=True):
            username: str
            password: HashedPassword
    """

    @classmethod
    def __get_validators__(cls):
        # One or more validators may be yielded which will be called in the
        # Order to vaidate the input, each validator will receive as an input
        # The value returned from the previous validator
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """ Accepts a plain text password and returns a hashed password """
        if not isinstance(v, str):
            raise TypeError("string required")

        hashed_password = get_password_hash(v)
        # You could also return a string here which would mean model.password
        # Would be a string, pydantic won't care but you could end up with some
        # Confusion since the value's type won't match the type annotation
        # exactly
        return cls(hashed_password)
