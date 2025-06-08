from sqlalchemy import Text, BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    social_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=True)
    registration_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    taps: Mapped[int] = mapped_column(BigInteger, default=0)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    info: Mapped[str] = mapped_column(Text, nullable=True)
    photo: Mapped[str] = mapped_column(Text, nullable=True)
