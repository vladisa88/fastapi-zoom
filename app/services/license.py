from random import choice

from services.base import Base
from models.license import LicenseAccount


class LicenseAccountService(Base):
    model = LicenseAccount

    async def get_random_account(self) -> LicenseAccount:
        accounts = await self.fetch_all()
        email = choice(accounts)
        await email.update(is_using=True)
        return email

account_service = LicenseAccountService()
