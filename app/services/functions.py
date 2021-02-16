import os
import asyncio

from models.license import LicenseAccount


def get_accounts() -> list[str]:
    """
    Fetch accounts from environment
    """
    accounts = os.environ["ACCOUNTS"]
    return accounts.split(",")


async def create_accounts_task() -> list:
    """
    Create async tasks for creating object in database
    """
    accounts = get_accounts()
    tasks = []
    for acc in accounts:
        task = asyncio.create_task(LicenseAccount.objects.create(email=acc))
        tasks.append(task)
    return tasks
