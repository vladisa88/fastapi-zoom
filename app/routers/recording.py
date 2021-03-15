# pylint:disable=(missing-function-docstring)
from fastapi import APIRouter

from services.recording import fetch_recording

recording_router = APIRouter()


@recording_router.get('/recording')
async def fetch_meeting_recording(meeting_id: str):
    return await fetch_recording(meeting_id)
