from app.domain.user import User
from app.domain.user_rating import UserRating
from infrastructure.db.uow import UnitOfWork


class UserGameService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_rating(self, social_id: int) -> UserRating:
        async with self.uow:
            total_taps = 0
            user_best = None
            user: User = await self.uow.users.get_rating(social_id)
            all_users: list[User] = await self.uow.users.list_all()
            if all_users is not None:
                total_taps = sum(user.taps for user in all_users)
                user_best = max(all_users, key=lambda u: u.taps)
            user_taps = user.taps
            return UserRating(user_taps, total_taps, user_best)
