import asyncio

from services.upload import uploader_service
from services.meeting import meeting_service


async def upload_recordings() -> None:
    """
    Periodically uploads recordings to Google Drive
    """
    meetings = await meeting_service.filter(is_downloaded=False)
    tasks = []
    for meeting in meetings:
        task = asyncio.create_task(uploader_service.upload_video(meeting))
        tasks.append(task)
    await asyncio.gather(*tasks)
