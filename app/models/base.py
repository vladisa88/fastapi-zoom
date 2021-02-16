import ormar

from conf.db import database, metadata


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
