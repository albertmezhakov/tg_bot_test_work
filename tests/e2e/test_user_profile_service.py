from __future__ import annotations

import pytest

from app.domain.user import User
from app.use_cases.user_profile_service import UserProfileService
from infrastructure.db.uow import UnitOfWork


@pytest.mark.asyncio
async def test_update_profile_fields(uow):
    # Arrange
    await uow.users.create(User(social_id=200, username="bob"))
    await uow.commit()

    # Act
    svc = UserProfileService(uow)
    await svc.update_name(200, "Robert")
    await svc.update_info(200, "QA engineer from Berlin")
    await svc.update_photo(200, "https://example.com/avatar.png")

    # Assert
    user = await uow.users.get_by_social_id(200)

    assert user.name == "Robert"
    assert user.info == "QA engineer from Berlin"
    assert user.photo == "https://example.com/avatar.png"


@pytest.mark.asyncio
async def test_update_methods_raise_for_unknown_user(uow):
        svc = UserProfileService(uow)
        with pytest.raises(ValueError):
            await svc.update_name(404, "Ghost")
        with pytest.raises(ValueError):
            await svc.update_info(404, "Invisible")
        with pytest.raises(ValueError):
            await svc.update_photo(404, "none")
