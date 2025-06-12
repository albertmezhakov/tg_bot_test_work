from abc import ABC, abstractmethod

from app.domain.repositories.user_repository import AbstractUserRepository


class AbstractUnitOfWork(ABC):
    users: AbstractUserRepository

    async def __aenter__(self) -> "AbstractUnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def rollback(self) -> None:
        ...
