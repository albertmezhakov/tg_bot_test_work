from infrastructure.db import User
from infrastructure.db.uow import UnitOfWork


class UserProfileService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def update_name(self, user_id: int, name: str) -> None:
        async with self.uow:
            user = await self.uow.users.get_by_social_id(user_id)
            user.name = name
            await self.uow.commit()

    async def update_info(self, user_id: int, info: str) -> None:
        async with self.uow:
            user = await self.uow.users.get_by_social_id(user_id)
            user.info = info
            await self.uow.commit()

    async def update_photo(self, user_id: int, photo_url: str) -> None:
        async with self.uow:
            user = await self.uow.users.get_by_social_id(user_id)
            user.photo = photo_url
            await self.uow.commit()
