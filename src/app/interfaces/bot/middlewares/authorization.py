from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.domain.auth_result import AuthStatus
from app.use_cases.user_auth_service import UserAuthService
from infrastructure.db.session import AsyncSessionLocal
from infrastructure.db.uow import UnitOfWork


class AuthorizationMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data):
        auth_service = data["user_auth_service"]

        user_id = event.from_user.id
        username = event.from_user.username
        passphrase = event.text.lower() if event.text else None

        auth_result = await auth_service.check_or_register(
            user_id=user_id,
            username=username,
            passphrase=passphrase,
        )
        if auth_result.status == AuthStatus.SUCCESS:
            return await handler(event, data)

        await event.answer(auth_result.message)
        return None
