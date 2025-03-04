from datetime import datetime
from typing import NewType
from uuid import UUID

from src.backend.domain.common import Base
from src.backend.domain.models import OrderItem, UserID
from src.backend.domain.value_objects import OrderStatus

OrderID = NewType("OrderID", UUID)


# TODO
class ShoppingCart(Base): ...


class Order(Base):
    id: OrderID
    user_id: UserID
    items: OrderItem
    status: OrderStatus
    takeout_time: datetime
