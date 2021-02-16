import os
import asyncio

from models.license import LicenseAccount


def get_accounts() -> list[str]:
    accounts = os.environ["ACCOUNTS"]
    return accounts.split(",")


async def create_accounts_task() -> list:
    accounts = get_accounts()
    tasks = []
    for acc in accounts:
        task = asyncio.create_task(LicenseAccount.objects.create(email=acc))
        tasks.append(task)
    return tasks
