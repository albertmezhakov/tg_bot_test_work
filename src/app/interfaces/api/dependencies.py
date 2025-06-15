from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.uow import AbstractUnitOfWork
from app.use_cases.user_game_service import UserGameService
from app.use_cases.user_profile_service import UserProfileService
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_uow(session: Annotated[AsyncSession, Depends(get_session)]) -> AsyncGenerator[AbstractUnitOfWork, None]:
    async with UnitOfWork(session) as uow:
        yield uow


def get_profile_service(
    uow: Annotated[AbstractUnitOfWork, Depends(get_uow)],
) -> UserProfileService:
    return UserProfileService(uow)


def get_game_service(
    uow: Annotated[AbstractUnitOfWork, Depends(get_uow)],
) -> UserGameService:
    return UserGameService(uow)
