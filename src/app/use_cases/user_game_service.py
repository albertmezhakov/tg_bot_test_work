from collections.abc import Sequence

from app.domain.uow import AbstractUnitOfWork
from app.domain.user import User
from app.domain.user_rating import UserRating


class UserGameService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def get_rating(self, social_id: int) -> UserRating | None:
        total_taps = 0
        user_best = None
        user: User = await self.uow.users.get_by_social_id(social_id)
        if user is None:
            return None
        all_users: Sequence[User] = await self.uow.users.list_all()
        if all_users is not None:
            total_taps = sum(user.taps for user in all_users)
            user_best = max(all_users, key=lambda u: u.taps)
        user_taps = user.taps
        return UserRating(user_taps, total_taps, user_best)

    async def register_tap(self, user_id: int) -> User | None:
        return await self.uow.users.add_tap(user_id)
