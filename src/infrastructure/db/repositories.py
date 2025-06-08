from typing import Any, Coroutine, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_social_id(self, social_id: int) -> User | None:
        stmt = select(User).where(User.social_id == social_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, user: User, **kwargs) -> User | None:
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.session.add(user)
        await self.session.flush()
        return user

    async def delete(self, user: User) -> User | None:
        await self.session.delete(user)

    async def list_all(self) -> Sequence[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()
