# pylint:disable=(too-few-public-methods)
import typing as tp

from pydantic import BaseModel


class StatisticModel(BaseModel):
    """
    Model describe schema of the
    `/statistic/` response
    """

    lesson: dict
    participants: tp.Optional[dict]
