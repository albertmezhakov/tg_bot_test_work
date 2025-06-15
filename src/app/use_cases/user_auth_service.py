from datetime import datetime

from app.domain.auth_result import AuthResult, AuthStatus
from app.domain.user import User
from config import settings
from infrastructure.db.uow import UnitOfWork


class UserAuthService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def check_or_register(self, user_id: int, username: str | None, passphrase: str | None) -> AuthResult:
        user_exists = await self.uow.users.exists_by_social_id(user_id)
        if user_exists:
            return AuthResult(AuthStatus.SUCCESS)
        if settings.register_passphrase and passphrase != settings.register_passphrase:
            return AuthResult(AuthStatus.NEED_PASSPHRASE, "Enter passphrase for register in bot:")
        if not username:
            return AuthResult(
                AuthStatus.NEED_USERNAME,
                "Для регистрации заполните, пожалуйста, Имя пользователя в своем профиле, иначе вас не смогут найти другие участники!",
            )
        await self.uow.users.create(User(social_id=user_id, username=username, registration_date=datetime.now()))
        await self.uow.commit()
        return AuthResult(AuthStatus.REGISTERED, "Welcome to bot")
