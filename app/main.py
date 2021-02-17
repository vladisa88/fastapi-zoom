from fastapi import FastAPI

from conf.db import database, metadata, engine
from conf.settings import CONFIG

from routers.zoom import zoom_router
from routers.license import account_router
from routers.statistic import statistic_router

app = FastAPI(
    title=CONFIG.title, description=CONFIG.description, version=CONFIG.version
)


metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    """
    Create database connection
    """
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """
    Disconnect from database
    """
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(zoom_router, tags=["meetings"])

app.include_router(account_router, tags=["accounts"])

app.include_router(statistic_router, tags=["statistics"])
