from decimal import Decimal
from typing import NewType, Optional
from uuid import UUID

from pydantic import EmailStr, HttpUrl, field_validator

from src.backend.domain.common import Base
from src.backend.domain.value_objects import UserRole

UserID = NewType("UserID", UUID)
CategoryID = NewType("CategoryID", UUID)
DishID = NewType("DishID", UUID)


class User(Base):
    id: UserID
    role: UserRole
    email: EmailStr


class Category(Base):
    id: CategoryID
    name: str


class Dish(Base):
    id: DishID
    name: str
    banner_path: Optional[str]
    price: Decimal
    description: Optional[str]
    weight: Optional[int]


class ShoppingCartItem(Base):
    dish: Dish
    amount: int
