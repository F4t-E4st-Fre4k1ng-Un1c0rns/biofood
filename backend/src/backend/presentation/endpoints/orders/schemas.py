from pydantic import BaseModel

from src.backend.domain.value_objects import OrderStatus


class ChangeOrderStatusInput(BaseModel):
    status: OrderStatus
