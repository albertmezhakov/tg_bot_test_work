from datetime import datetime

from app.domain.user import User
from config import settings


class UserAuthService:
    def __init__(self, uow):
        self.uow = uow

    async def check_or_register(self, user_id: int, username: str | None, passphrase: str | None) -> tuple[
        bool, str | None]:
        async with self.uow:
            user_exists = await self.uow.users.exists_by_social_id(user_id)
            if user_exists:
                return True, None
            if settings.register_passphrase and passphrase != settings.register_passphrase:
                return False, "Enter passphrase for register in bot:"
            if not username:
                return False, (
                    "Для регистрации заполните, пожалуйста, Имя пользователя в своем профиле, "
                    "иначе вас не смогут найти другие участники!"
                )
            await self.uow.users.create(User(
                social_id=user_id,
                username=username,
                registration_date=datetime.now()
            ))
            await self.uow.commit()
            return False, "Welcome to bot"
