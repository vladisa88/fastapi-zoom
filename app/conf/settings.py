# pylint:disable=(invalid-name, too-few-public-methods)
# pylint:disable=(missing-class-docstring)
import os

from conf.vars import DESCRIPTION, TITLE, VERSION


class Config:
    def __init__(self) -> None:
        self.title = TITLE
        self.description = DESCRIPTION
        self.version = VERSION
        self.port = int(os.environ["BACK_END_PORT"])
        self.zoon_token = os.environ["ZOOM_TOKEN"]


CONFIG = Config()


class PostgresConfig:
    def __init__(self) -> None:
        self.host = os.environ["POSTGRES_HOST"]
        self.port = int(os.environ["POSTGRES_PORT"])
        self.db = os.environ["POSTGRES_DB"]
        self.user = os.environ["POSTGRES_USER"]
        self.password = os.environ["POSTGRES_PASSWORD"]

        self.url = (
            f"postgresql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.db}"
        )


POSTGRES_CONFIG = PostgresConfig()
