# pylint:disable=(invalid-name, too-few-public-methods, too-many-ancestors)
import ormar
from pydantic import EmailStr

from models.base import BaseMeta


class LicenseAccount(ormar.Model):
    """
    Describe `LicenseAccount` model in database
    """
    class Meta(BaseMeta):
        # pylint:disable=(missing-class-docstring)
        pass

    id: int = ormar.Integer(primary_key=True)
    email: EmailStr = ormar.String(max_length=50)
    is_using: bool = ormar.Boolean(default=False)
