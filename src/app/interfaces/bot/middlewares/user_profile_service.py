from aiogram import BaseMiddleware
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork
from app.services.user_profile_service import UserProfileService

class UserProfileServiceMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with AsyncSessionLocal() as session:
            uow = UnitOfWork(session)
            data["user_profile_service"] = UserProfileService(uow)
            return await handler(event, data)