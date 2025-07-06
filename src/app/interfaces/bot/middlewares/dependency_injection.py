from aiogram import BaseMiddleware

from app.use_cases.user_auth_service import UserAuthService
from app.use_cases.user_game_service import UserGameService
from app.use_cases.user_profile_service import UserProfileService
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork


class DependencyInjectionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with AsyncSessionLocal() as session:
            async with UnitOfWork(session) as uow:
                data["user_profile_service"] = UserProfileService(uow)
                data["user_game_service"] = UserGameService(uow)
                data["user_auth_service"] = UserAuthService(uow)
                return await handler(event, data)
