# pylint:disable=(too-few-public-methods)
from pydantic import BaseModel


class UpdateAccount(BaseModel):
    """
    Schema for updating the status of account model
    """
    email: str = "example@test.com"
