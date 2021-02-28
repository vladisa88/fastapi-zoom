# pylint:disable=(missing-function-docstring)
from fastapi import APIRouter

from services.statistic import fetch_statistic
from services.statistic import fetch_statistic_by_course_code

from schemas.statistic import StatisticCourseCodeModel
from schemas.statistic import StatisticResponseModel

statistic_router = APIRouter()


@statistic_router.get("/statistic", response_model=StatisticResponseModel)
async def statistic(meeting_id: str):
    return await fetch_statistic(meeting_id)


@statistic_router.post("/statistic")
async def statistic_by_discipline(body: StatisticCourseCodeModel):
    return await fetch_statistic_by_course_code(body.course_code)
