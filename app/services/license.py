from random import choice
from fastapi_ormar_utilities import Base

from models.license import LicenseAccount


class LicenseAccountService(Base):
    """
    Service expands base logic for
    license accounts
    """

    model = LicenseAccount

    async def get_random_account(self) -> LicenseAccount:
        """
        Choose random account and return it
        """
        accounts = await self.fetch_all()
        email = choice(accounts)
        await email.update(is_using=True)
        return email


account_service = LicenseAccountService()
