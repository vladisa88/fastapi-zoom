import os

from aiozoom import Zoom


class ZoomService:
    """
    Configure aiozoom object and request body
    for requests to Zoom API
    """

    ZOOM_TOKEN = os.environ["ZOOM_TOKEN"]

    def __init__(self):
        Zoom.configure(self.ZOOM_TOKEN)
        self.__zoom = Zoom()

    @property
    def zoom(self) -> Zoom:
        """
        Return aiozoom Zoom object
        """
        return self.__zoom

    @staticmethod
    def body(title) -> dict:
        """
        Create body for requests
        """
        return {
            "topic": title,
            "type": 2,
            "timezone": "Europe/Moscow",
            "settings": {
                "auto_recording": "cloud",
                "waiting_room": False,
                "meeting_authentication": True,
                "join_before_host": True,
            },
        }


zoom_service = ZoomService()
