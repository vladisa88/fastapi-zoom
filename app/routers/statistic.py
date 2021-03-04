# pylint:disable=(missing-function-docstring)
from fastapi import APIRouter

from services.statistic import fetch_statistic

statistic_router = APIRouter()


@statistic_router.get("/statistic")
async def fetch_meeting_statistic(meeting_id: str):
    return await fetch_statistic(meeting_id)
