import asyncio

from fastapi import APIRouter

from services.license import LicenseAccountService
from services.functions import create_accounts_task

from models.license import LicenseAccount

account_router = APIRouter()
account_service = LicenseAccountService()

@account_router.post('/populate')
async def create_accounts():
    tasks = await create_accounts_task()
    await asyncio.gather(*tasks)


@account_router.get('/accounts')
async def fetch_accounts():
    return await account_service.fetch_all()
