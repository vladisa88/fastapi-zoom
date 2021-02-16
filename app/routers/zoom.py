# pylint:disable=(missing-function-docstring)
import asyncio

from fastapi import APIRouter

from schemas.zoom import CreateMeetingModel, ResponseMeetingModel, StopMeetingModel

from models.zoom import Meeting

from services.meeting import meeting_service
from services.zoom import zoom_service

zoom_router = APIRouter()


@zoom_router.post("/meeting", response_model=ResponseMeetingModel)
async def create_meeting(data: CreateMeetingModel):
    return await meeting_service.create(data)


@zoom_router.get("/meetings")
async def fetch_meetings():
    return await meeting_service.fetch_all()


@zoom_router.delete("/meeting/{meeting_id}")
async def stop_meeting(meeting_id: str):
    return await zoom_service.zoom.stop_meeting(meeting_id)


@zoom_router.put("/meetings")
async def stop_all_meetings(data: StopMeetingModel):
    tasks = []
    live_meetings = await Meeting.objects.exclude(meeting_id__in=data.meetings_id).all()
    for meeting in live_meetings:
        task = asyncio.create_task(meeting_service.stop(meeting.meeting_id))
        tasks.append(task)
    await asyncio.gather(*tasks)
    return {"status": "success"}
