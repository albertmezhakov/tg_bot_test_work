from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Union

from app.domain.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_by_social_id(self, social_id: int) -> User | None:
        ...

    @abstractmethod
    async def add_tap(self, social_id: int) -> Union[User, None]:
        ...

    @abstractmethod
    async def exists_by_social_id(self, user_id: int) -> bool:
        ...

    @abstractmethod
    async def create(self, user: User) -> User:
        ...

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        ...

    @abstractmethod
    async def update(self, user: User) -> None:
        ...

    @abstractmethod
    async def list_all(self) -> Sequence[User]:
        ...
