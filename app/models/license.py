import ormar
from pydantic import EmailStr

from models.base import BaseMeta


class LicenseAccount(ormar.Model):
    class Meta(BaseMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    email: EmailStr = ormar.String(max_length=50)
    is_using: bool = ormar.Boolean(default=False)
