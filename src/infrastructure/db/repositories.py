from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from app.domain.user import User as DomainUser
from infrastructure.db.models import User as ORMUser


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_social_id(self, social_id: int) -> DomainUser | None:
        stmt = select(ORMUser).where(ORMUser.social_id == social_id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        return self._to_domain(orm_user) if orm_user else None

    async def add_tap(self, social_id: int) -> DomainUser | None:
        stmt = (
            update(ORMUser)
            .where(ORMUser.social_id == social_id)
            .values(taps=ORMUser.taps + 1)
            .returning(ORMUser)
        )
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        await self.session.commit()

        return self._to_domain(orm_user) if orm_user else None

    async def exists_by_social_id(self, user_id: int) -> bool:
        stmt = select(ORMUser.id).where(ORMUser.social_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none() is not None

    async def create(self, domain_user: DomainUser) -> DomainUser:
        orm_user = ORMUser(
            social_id=domain_user.social_id,
            username=domain_user.username,
            registration_date=domain_user.registration_date,
            taps=domain_user.taps,
            name=domain_user.name,
            info=domain_user.info,
            photo=domain_user.photo,
        )
        self.session.add(orm_user)
        await self.session.flush()
        return self._to_domain(orm_user)

    async def delete(self, user_id: int) -> None:
        stmt = select(ORMUser).where(ORMUser.id == user_id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        if orm_user:
            await self.session.delete(orm_user)

    async def update(self, domain_user: DomainUser) -> None:
        stmt = select(ORMUser).where(ORMUser.id == domain_user.id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        if orm_user:
            orm_user.username = domain_user.username
            orm_user.registration_date = domain_user.registration_date
            orm_user.taps = domain_user.taps
            orm_user.name = domain_user.name
            orm_user.info = domain_user.info
            orm_user.photo = domain_user.photo

    async def list_all(self) -> Sequence[DomainUser]:
        result = await self.session.execute(select(ORMUser))
        return [self._to_domain(orm_user) for orm_user in result.scalars().all()]

    @staticmethod
    def _to_domain(orm_user: ORMUser) -> DomainUser:
        return DomainUser(
            id=orm_user.id,
            social_id=orm_user.social_id,
            username=orm_user.username,
            registration_date=orm_user.registration_date,
            taps=orm_user.taps,
            name=orm_user.name,
            info=orm_user.info,
            photo=orm_user.photo,
        )
