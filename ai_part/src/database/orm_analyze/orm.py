from uuid import UUID
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase): ...


class AIData(Base):
    __tablename__ = "ai_data"
    id: Mapped[int] = mapped_column(primary_key=True)
    ds: Mapped[datetime] = mapped_column(unique=True)
    yhat_lower: Mapped[int]
    yhat_upper: Mapped[int]
    yhat: Mapped[int]

    dish_id: Mapped[UUID]
    dish_name: Mapped[str] = mapped_column(String(120))
