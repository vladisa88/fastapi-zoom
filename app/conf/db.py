import databases
import sqlalchemy

from conf.settings import POSTGRES_CONFIG

# settings = get_settings()

metadata = sqlalchemy.MetaData()
database = databases.Database(POSTGRES_CONFIG.url)
engine = sqlalchemy.create_engine(POSTGRES_CONFIG.url)
