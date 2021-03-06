import asyncio
import typing as tp
from datetime import date

from fastapi import HTTPException, status

from services.meeting import meeting_service
from services.zoom import zoom_service

from schemas.statistic import StatisticModel


class StatisticService:
    """
    Contains some methods for interaction with
    Zoom dashboard API
    """

    async def fetch_statistic(self, meeting_id: str) -> StatisticModel:
        """
        Get information about past meeting
        """
        participation = await zoom_service.zoom.get_meeting_participants(
            meeting_id
        )
        participants = participation.get("participants", None)
        lesson = await zoom_service.zoom.get_meeting_info(meeting_id)
        return StatisticModel(lesson=lesson, participants=participants)

    async def fetch_statistic_with_params(
        self,
        date_from: date,
        date_to: date,
        course_code: tp.Optional[str],
        lesson_title: tp.Optional[str],
    ) -> list[dict]:
        """
        Get information about searched meetings
        """
        base_kwargs = {
            "created__gte": str(date_from),
            "created__lte": str(date_to),
        }

        if course_code:
            base_kwargs["course_code"] = course_code

        if lesson_title:
            base_kwargs["lesson_title"] = lesson_title

        meetings = await meeting_service.filter(**base_kwargs)

        tasks = []
        meeting_ids = [m.meeting_id for m in meetings]

        if not meeting_ids:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Items not found"
            )

        for m_id in meeting_ids:
            task = asyncio.create_task(self.fetch_statistic(m_id))
            tasks.append(task)
        return await asyncio.gather(*tasks)


statistic_servive = StatisticService()
