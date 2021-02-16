import typing as tp

import ormar
from pydantic import BaseModel


class Base:
    model: ormar.Model

    async def fetch_all(self) -> tp.List[ormar.Model]:
        return await self.model.objects.all()

    async def create(self, schema: BaseModel, **kwargs: tp.Any) -> ormar.Model:
        obj = await self.model.objects.create(
            **schema.dict(exclude_unset=True), **kwargs
        )
        return obj

    async def fetch_one(self, unique_id: int) -> ormar.Model:
        return await self.model.objects.get(pk=unique_id)

    async def fetch_one_by_param(self, **kwargs) -> ormar.Model:
        return await self.model.objects.get(**kwargs)

    async def filter(self, **kwargs) -> ormar.Model:
        return await self.model.objects.all(**kwargs)

    async def update(self, unique_id: int, schema: BaseModel) -> ormar.Model:
        obj = await self.fetch_one(unique_id)
        return await obj.update(schema.dict(exclude_unset=True))

    async def delete(self, unique_id: int) -> None:
        obj = await self.fetch_one(unique_id)
        await obj.delete()
