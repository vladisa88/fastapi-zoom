# pylint:disable=(missing-function-docstring)
from fastapi import APIRouter

from schemas.zoom import CreateMeetingModel, ResponseMeetingModel, StopMeetingModel

from services.meeting import meeting_service
from services.zoom import zoom_service

zoom_router = APIRouter()


@zoom_router.get("/meetings")
async def fetch_meetings():
    return await meeting_service.fetch_all()


@zoom_router.post("/meeting", response_model=ResponseMeetingModel)
async def create_meeting(data: CreateMeetingModel):
    return await meeting_service.create(data)


@zoom_router.put("/meetings")
async def stop_all_meetings(data: StopMeetingModel):
    return await meeting_service.stop_list_of_meetings(data)


@zoom_router.delete("/meeting/{meeting_id}")
async def stop_meeting(meeting_id: str):
    return await zoom_service.zoom.stop_meeting(meeting_id)
