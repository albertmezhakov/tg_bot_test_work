from __future__ import annotations

import pytest

from tests_utils.dummy_config import dummy_config

dummy_config()
from app.domain.auth_result import AuthStatus
from app.use_cases.user_auth_service import UserAuthService
from infrastructure.db.uow import UnitOfWork


@pytest.mark.asyncio
async def test_successful_registration_and_subsequent_success(session_factory):
    async with session_factory() as session:
        svc = UserAuthService(UnitOfWork(session))
        first = await svc.check_or_register(1, "anton", "secret")
    assert first.status is AuthStatus.REGISTERED

    async with session_factory() as session:
        svc = UserAuthService(UnitOfWork(session))
        second = await svc.check_or_register(1, "anton", "secret")
    assert second.status is AuthStatus.SUCCESS


@pytest.mark.asyncio
async def test_need_passphrase_if_wrong_passphrase(session_factory):
    async with session_factory() as session:
        svc = UserAuthService(UnitOfWork(session))
        result = await svc.check_or_register(2, "albert", "wrong")
    assert result.status is AuthStatus.NEED_PASSPHRASE


@pytest.mark.asyncio
async def test_need_username_if_username_missing(session_factory):
    async with session_factory() as session:
        svc = UserAuthService(UnitOfWork(session))
        result = await svc.check_or_register(3, None, "secret")
    assert result.status is AuthStatus.NEED_USERNAME
