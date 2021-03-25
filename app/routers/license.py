# pylint:disable=(missing-function-docstring)
import asyncio

from fastapi import APIRouter

from schemas.license import UpdateAccount

from services.functions import create_accounts_task
from services.license import LicenseAccountService

account_router = APIRouter()
account_service = LicenseAccountService()


@account_router.post("/populate")
async def create_accounts():
    tasks = await create_accounts_task()
    await asyncio.gather(*tasks)


@account_router.get("/accounts")
async def fetch_accounts():
    return await account_service.fetch_all(related_field="meetings")


@account_router.get("/accounts/{primary_key}")
async def fetch_one_account(primary_key: int):
    return await account_service.fetch_one(primary_key, "meetings")


@account_router.patch("/accounts/")
async def patch_status(data: UpdateAccount):
    return await account_service.patch_status(data)
