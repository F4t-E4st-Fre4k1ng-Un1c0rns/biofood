from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from src.backend.adapters.database.orm.common import utcnow


class UUIDMixin:
    id: Mapped[UUID] = mapped_column(
        "id",
        primary_key=True,
        default=uuid4,
        nullable=False,
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        "createdAt",
        nullable=False,
        server_default=utcnow(),
        sort_order=9999,
    )
    updated_at: Mapped[datetime] = mapped_column(
        "updatedAt",
        nullable=True,
        server_default=utcnow(),
        server_onupdate=utcnow(),
        sort_order=10000,
    )
