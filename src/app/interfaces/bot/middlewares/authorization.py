from aiogram import BaseMiddleware
from aiogram.types import Message

from app.use_cases.user_auth_service import UserAuthService
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork


class AuthorizationMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        async with AsyncSessionLocal() as session:
            uow = UnitOfWork(session)
            auth_service = UserAuthService(uow)
            is_auth, response = await auth_service.check_or_register(
                user_id=event.from_user.id,
                username=event.from_user.username,
                passphrase=event.text.lower() if event.text else None,
            )
            if is_auth:
                return await handler(event, data)
            if response:
                await event.answer(response)
            return None
