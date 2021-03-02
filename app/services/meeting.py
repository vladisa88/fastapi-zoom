import typing as tp

from pydantic import BaseModel
import ormar
from fastapi_ormar_utilities import Base

from services.license import account_service
from services.zoom import zoom_service

from models.zoom import Meeting


class MeetingService(Base):
    """
    Service for expanding base logic for
    Zoom meetings
    """

    model = Meeting

    async def create(self, schema: BaseModel, **kwargs: tp.Any) -> ormar.Model:
        """
        Create meeting using `aiozoom`, create `Meeting` object
        """
        # pylint:disable=(no-member)
        body = zoom_service.body(schema.title)
        account = await account_service.get_random_account()
        meeting = await zoom_service.zoom.create_meeting(account.email, body)
        obj = await self.model.objects.create(
            **schema.dict(exclude_unset=True),
            meeting_id=str(meeting.get("id")),
            start_url=meeting.get("start_url"),
            join_url=meeting.get("join_url"),
            email=account,
            **kwargs
        )
        return obj

    async def stop(self, meeting_id: str) -> None:
        """
        Stop the meeting using `aiozoom`, update objects in database
        """
        meeting = await self.fetch_one_by_param(meeting_id=meeting_id)
        account = await account_service.fetch_one(meeting.email.id)
        await meeting.update(is_active=False)
        await account.update(is_using=False)
        await zoom_service.zoom.stop_meeting(meeting_id)
        return


meeting_service = MeetingService()
