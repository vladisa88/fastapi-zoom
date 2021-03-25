import asyncio
import typing as tp

import ormar

from fastapi_ormar_utilities import Base

from pydantic import BaseModel

from models.zoom import Meeting

from schemas.zoom import StopMeetingModel

from services.license import account_service
from services.zoom import zoom_service


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

    async def stop_all(self, meetings: StopMeetingModel) -> dict:
        """
        Stop all meetings that are not included in request
        """
        tasks = []
        live_meetings = await Meeting.objects.exclude(
            meeting_id__in=meetings.meetings_id
        ).all()
        for meeting in live_meetings:
            task = asyncio.create_task(
                meeting_service.stop(meeting.meeting_id)
            )
            tasks.append(task)
        await asyncio.gather(*tasks)
        return {"status": "success"}


meeting_service = MeetingService()
