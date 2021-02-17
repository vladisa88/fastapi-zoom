from services.zoom import zoom_service


async def fetch_statistic(meeting_id: str) -> dict:
    """
    Get information about past meeting
    """
    return await zoom_service.zoom.get_meeting_participants(meeting_id)
