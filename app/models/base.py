import ormar
from conf.db import database, metadata


class BaseMeta(ormar.ModelMeta):
    """
    Base Meta class for future models
    """

    # pylint:disable=(too-few-public-methods)
    database = database
    metadata = metadata
