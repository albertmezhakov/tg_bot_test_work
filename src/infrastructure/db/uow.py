from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories.user_repository import AbstractUserRepository
from app.domain.uow import AbstractUnitOfWork
from infrastructure.db.repositories import UserRepository


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users: AbstractUserRepository = UserRepository(self.session)

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
