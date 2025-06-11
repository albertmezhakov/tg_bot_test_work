from dataclasses import dataclass

from app.domain.user import User


@dataclass
class UserRating:
    user_taps: int
    total_taps: int
    user_best: User | None = None
