import asyncio
import typing as tp
from datetime import date

from services.zoom import zoom_service
from services.meeting import meeting_service

class StatisticService:
    """
    Contains some methods for interaction with
    Zoom dashboard API
    """

    async def fetch_statistic(self, meeting_id: str) -> dict:
        """
        Get information about past meeting
        """
        return await zoom_service.zoom.get_meeting_participants(meeting_id)

    async def fetch_statistic_with_params(
        self,
        date_from: date,
        date_to: date,
        course_code: tp.Optional[str],
        lesson_title: tp.Optional[str]
    ) -> list[dict]:
        """
        Get information about searched meetings
        """
        base_kwargs = {
            "created__gte": str(date_from),
            "created__lte": str(date_to)
        }
        if course_code:
            meetings = await meeting_service.filter(
                course_code=course_code,
                **base_kwargs
            )
        elif lesson_title:
            meetings = await meeting_service.filter(
                lesson_title=lesson_title,
                **base_kwargs
            )
        else:
            meetings = await meeting_service.filter(
                **base_kwargs
            )

        tasks = []
        meeting_ids = [m.meeting_id for m in meetings]
        for m_id in meeting_ids:
            task = asyncio.create_task(
                self.fetch_statistic(m_id)
            )
            tasks.append(task)
        return await asyncio.gather(*tasks)


statistic_servive = StatisticService()
