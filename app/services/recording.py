from services.zoom import zoom_service


async def fetch_recording(meeting_id: str) -> dict:
    """
    Get information about past meeting recording
    """
    return await zoom_service.zoom.get_recording(meeting_id)
