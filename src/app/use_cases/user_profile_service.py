from app.domain.uow import AbstractUnitOfWork
from app.domain.user import User
from infrastructure.db.uow import UnitOfWork


class UserProfileService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def update_name(self, user_id: int, name: str) -> None:
        async with self.uow:
            user: User | None = await self.uow.users.get_by_social_id(user_id)
            if user is None:
                raise ValueError("User not found")
            user.name = name
            await self.uow.users.update(user)
            await self.uow.commit()

    async def update_info(self, user_id: int, info: str) -> None:
        async with self.uow:
            user: User | None = await self.uow.users.get_by_social_id(user_id)
            if user is None:
                raise ValueError("User not found")
            user.info = info
            await self.uow.users.update(user)
            await self.uow.commit()

    async def update_photo(self, user_id: int, photo_url: str) -> None:
        async with self.uow:
            user: User | None = await self.uow.users.get_by_social_id(user_id)
            if user is None:
                raise ValueError("User not found")
            user.photo = photo_url
            await self.uow.users.update(user)
            await self.uow.commit()
