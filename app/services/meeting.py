import typing as tp

from pydantic import BaseModel
import ormar

from services.base import Base
from services.license import account_service
from services.zoom import zoom_service

from models.zoom import Meeting

from aiozoom import Zoom


class MeetingService(Base):
    model = Meeting

    async def create(self, schema: BaseModel, **kwargs: tp.Any) -> ormar.Model:
        body = zoom_service.body(schema.title)
        account = await account_service.get_random_account()
        meeting = await zoom_service.zoom.create_meeting(account.email, body)
        obj = await self.model.objects.create(
            **schema.dict(exclude_unset=True),
            meeting_id=str(meeting.get('id')),
            start_url=meeting.get('start_url'),
            join_url=meeting.get('join_url'),
            email=account,
            **kwargs)
        return obj

    async def stop(self, meeting_id: str) -> None:
        meeting = await self.fetch_one_by_param(
            meeting_id=meeting_id)
        account = await account_service.fetch_one(
            meeting.email.id)
        await meeting.update(is_active=False)
        await account.update(is_using=False)
        await zoom_service.zoom.stop_meeting(meeting_id)
        return

meeting_service = MeetingService()
