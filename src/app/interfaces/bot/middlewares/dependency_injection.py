from aiogram import BaseMiddleware

from app.domain.uow import AbstractUnitOfWork
from app.use_cases.user_game_service import UserGameService
from app.use_cases.user_profile_service import UserProfileService
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork


class DependencyInjectionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with AsyncSessionLocal() as session:
            uow: AbstractUnitOfWork = UnitOfWork(session)
            data["user_profile_service"] = UserProfileService(uow)
            data["user_game_service"] = UserGameService(uow)
            return await handler(event, data)
