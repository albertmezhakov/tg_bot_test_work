from app.domain.uow import AbstractUnitOfWork
from app.domain.user import User


class UserProfileService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def get_user(self, user_id: int) -> User | None:
        user: User | None = await self.uow.users.get_by_social_id(user_id)
        return user

    async def update_name(self, user_id: int, name: str) -> User | None:
        user: User | None = await self.uow.users.get_by_social_id(user_id)
        if user is None:
            raise ValueError("User not found")
        user.name = name
        await self.uow.users.update(user)
        await self.uow.commit()
        return user

    async def update_info(self, user_id: int, info: str) -> User | None:
        user: User | None = await self.uow.users.get_by_social_id(user_id)
        if user is None:
            raise ValueError("User not found")
        user.info = info
        await self.uow.users.update(user)
        await self.uow.commit()
        return user

    async def update_photo(self, user_id: int, photo_url: str) -> User | None:
        user: User | None = await self.uow.users.get_by_social_id(user_id)
        if user is None:
            raise ValueError("User not found")
        user.photo = photo_url
        await self.uow.users.update(user)
        await self.uow.commit()
        return user
