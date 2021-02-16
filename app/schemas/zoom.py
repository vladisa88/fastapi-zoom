import typing as tp
from pydantic import BaseModel, Field


class CreateMeetingModel(BaseModel):
    title: str
    course_code: str = Field(None, description='Course code from RUZ')
    calendar_id: str = Field(None, description='Calendar ID for google')
    event_id: str = Field(None, description='Event ID for google')


class ResponseMeetingModel(BaseModel):
    id: int = 1
    meeting_id: str = '99966866119'
    title: str = 'Физика 3 курс'
    calendar_id: tp.Optional[str] = 'some data'
    event_id: tp.Optional[str] = 'some data'
    course_code: tp.Optional[str] = 'some data'
    start_url: str = 'https://zoom.us/j/99966866119'
    join_url: str = 'https://zoom.us/j/99966866119?xxxxxx'


class StopMeetingModel(BaseModel):
    meetings_id: list[str]
