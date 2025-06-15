from __future__ import annotations

import pytest

from app.domain.user import User
from app.use_cases.user_game_service import UserGameService


async def _bootstrap_sample_data(uow) -> None:
    await uow.users.create(User(social_id=1, username="anton", taps=10))
    await uow.users.create(User(social_id=2, username="alisa", taps=15))
    await uow.users.create(User(social_id=3, username="albert", taps=5))
    await uow.commit()


@pytest.mark.asyncio
async def test_register_tap_increments_taps(uow):
    await uow.users.create(User(social_id=1, username="albert"))
    await uow.commit()

    svc = UserGameService(uow)
    await svc.register_tap(1)
    user = await svc.register_tap(1)

    assert user.taps == 2


@pytest.mark.asyncio
async def test_register_tap_returns_none_for_unknown_user(uow):
    svc = UserGameService(uow)
    result = await svc.register_tap(2)
    assert result is None


@pytest.mark.asyncio
async def test_get_rating_returns_correct_aggregates(uow):
    await _bootstrap_sample_data(uow)

    rating = await UserGameService(uow).get_rating(1)
    assert rating.user_taps == 10
    assert rating.total_taps == 30
    assert rating.user_best.social_id == 2
    assert rating.user_best.taps == 15
