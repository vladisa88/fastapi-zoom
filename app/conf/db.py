import os

import databases
import sqlalchemy

if not bool(os.environ["IS_TEST"]):
    from conf.settings import POSTGRES_CONFIG

    DATABASE_URL = POSTGRES_CONFIG.url
else:
    DATABASE_URL = "sqlite:///test.db"

# settings = get_settings()

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
