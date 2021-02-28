import os

from aiohttp import ClientSession

from services.zoom import zoom_service

from models.zoom import Meeting


BACK_END_HOST = "back-end"
BACK_END_PORT = os.environ["BACK_END_PORT"]
BACK_END_URL = f"http://{BACK_END_HOST}:{BACK_END_PORT}/"
NVR_URL = "https://nvr.miem.hse.ru/api/fileuploader/files/"

ZOOM_TOKEN = os.environ["ZOOM_TOKEN"]
NVR_TOKEN = os.environ["NVR_TOKEN"]


class UploadService:
    """
    Provide methods for uploading recordings
    to NVR
    """

    __slots__ = (
        "_base_back_end_url",
        "_base_nvr_url",
        "_session",
        "_headers",
        "_zoom_token",
        "_chunk_size",
    )

    def __init__(self):
        self._base_back_end_url = BACK_END_URL
        self._base_nvr_url = NVR_URL
        self._session = ClientSession()
        self._headers = {"key": NVR_TOKEN}
        self._zoom_token = ZOOM_TOKEN
        self._chunk_size = 256 * 1024 * 25  # 5MB

    async def _fetch_download_url(self, meeting_id: str) -> str:
        """
        Get link to download the recording file
        """
        response = await zoom_service.zoom.get_recording(meeting_id)
        if "recording_files" not in response.keys():
            # raise error
            print(response)
        url = response["recording_files"][0]["download_url"]
        return self._give_access_to_url(url)

    def _give_access_to_url(self, url: str) -> str:
        """
        Add access token to download url
        to make it downloadable for external users
        """
        return f"{url}?access_token={self._zoom_token}"

    async def _fetch_recording(self, meeting_id: str) -> bytes:
        """
        Get video object in bytes
        """
        url = await self._fetch_download_url(meeting_id)
        async with self._session.get(url) as response:
            data = await response.read()
        return data

    @staticmethod
    def _create_request_body(data: Meeting, video: bytes) -> dict:
        """
        Request body for POST request to NVR
        """
        return {
            "file_name": data.title,
            "folder_name": data.course_code,
            "room_name": "Zoom",
            "file_size": len(video),
            "record_dt": data.created.isoformat().split(".")[0],
            "calendar_data": {
                "calendar_id": data.calendar_id,
                "event_id": data.event_id,
            },
        }

    async def _fetch_file_id(self, meeting: Meeting, video: bytes) -> str:
        """
        Get `file_id` from NVR for uploading
        """
        body = self._create_request_body(meeting, video)
        async with self._session.post(
            url=self._base_nvr_url, headers=self._headers, json=body, ssl=False
        ) as response:
            data = await response.json()
        return data["file_id"]

    async def upload_video(self, meeting: Meeting):
        """
        Upload video to Google Drive using NVR API
        """
        video = await self._fetch_recording(meeting.meeting_id)
        file_id = await self._fetch_file_id(meeting, video)
        url = f"{self._base_nvr_url}{file_id}"

        for chunck in video.iter_chuncked(self._chunk_size):
            async with self._session.put(
                url=url, data={"file_data": chunck}, ssl=False, headers=self._headers
            ) as response:
                print(await response.json())

        await meeting.update(is_downloaded=True)


uploader_service = UploadService()
