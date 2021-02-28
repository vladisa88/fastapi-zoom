# pylint:disable=(invalid-name, too-few-public-methods, too-many-ancestors)
from datetime import datetime

import ormar
from pydantic import EmailStr

from models.base import BaseMeta
from models.license import LicenseAccount


class Meeting(ormar.Model):
    """
    Describe `Meeting` model in database
    """

    class Meta(BaseMeta):
        # pylint:disable=(missing-class-docstring)
        pass

    id: int = ormar.Integer(primary_key=True)
    meeting_id: str = ormar.String(max_length=70)
    title: str = ormar.String(max_length=70)
    calendar_id: str = ormar.String(max_length=150, nullable=True)
    event_id: str = ormar.String(max_length=150, nullable=True)
    course_code: str = ormar.String(max_length=150, nullable=True)
    start_url: str = ormar.String(max_length=1000)
    join_url: str = ormar.String(max_length=100)
    created: str = ormar.DateTime(default=datetime.now())
    is_active: bool = ormar.Boolean(default=True)
    is_downloaded: bool = ormar.Boolean(default=False)
    email: EmailStr = ormar.ForeignKey(LicenseAccount)
