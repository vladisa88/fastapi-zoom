# pylint:disable=(missing-function-docstring)
import typing as tp
from datetime import date

from fastapi import APIRouter

from services.statistic import statistic_servive

statistic_router = APIRouter()


@statistic_router.get("/statistic/{meeting_id}")
async def fetch_meeting_statistic(meeting_id: str):
    return await statistic_servive.fetch_statistic(meeting_id)


@statistic_router.get("/statistic/")
async def fetch_meeting_statistic_query(
    date_from: date,
    date_to: date,
    course_code: tp.Optional[str] = None,
    lesson_title: tp.Optional[str] = None,
):
    return await statistic_servive.fetch_statistic_with_params(
        date_from, date_to, course_code, lesson_title
    )
