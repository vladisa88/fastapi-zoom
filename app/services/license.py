from random import choice

from fastapi import HTTPException, status
from fastapi_ormar_utilities import Base

from models.license import LicenseAccount
from schemas.license import UpdateAccount


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
        accounts = await self.filter(is_using=False)
        if not accounts:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="License accounts is over!"
            )
        email = choice(accounts)
        await email.update(is_using=True)
        return email

    async def patch_status(self, data: UpdateAccount) -> LicenseAccount:
        """
        Update account status to unused
        """
        account = await self.fetch_one_by_param(email=data.email)
        return await account.update(is_using=False)

account_service = LicenseAccountService()
