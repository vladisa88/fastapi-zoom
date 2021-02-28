import asyncio

from fastapi import HTTPException

from services.zoom import zoom_service
from services.meeting import meeting_service


async def fetch_statistic(meeting_id: str) -> dict:
    """
    Get information about past meeting
    """
    response = await zoom_service.zoom.get_meeting_participants(meeting_id)
    if "code" in response.keys():
        raise HTTPException(status_code=404, detail="Meeting not found!")


async def fetch_statistic_by_course_code(course_code: str) -> dict:
    """
    Get information about all meetings by discipline
    """
    meetings = await meeting_service.filter(course_code=course_code)
    if not meetings:
        raise HTTPException(
            status_code=404, detail="Meetings with such course code are not exist"
        )
    tasks = []
    for meeting in meetings:
        task = asyncio.create_task(
            zoom_service.zoom.get_meeting_participants(meeting.meeting_id)
        )
        tasks.append(task)
    return await asyncio.gather(*tasks)
