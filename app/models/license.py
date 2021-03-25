# pylint:disable=(invalid-name, too-few-public-methods, too-many-ancestors)
import ormar
from models.base import BaseMeta
from pydantic import EmailStr


class LicenseAccount(ormar.Model):
    """
    Describe `LicenseAccount` model in database
    """

    class Meta(BaseMeta):
        # pylint:disable=(missing-class-docstring)
        pass

    id: int = ormar.Integer(primary_key=True)
    email: EmailStr = ormar.String(max_length=45)
    is_using: bool = ormar.Boolean(default=False)
