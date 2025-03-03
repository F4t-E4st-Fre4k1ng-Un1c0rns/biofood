from abc import ABC, abstractmethod
from typing import Self

from src.backend.application.common.repository import Repository
from src.backend.domain.aggregates import Order
from src.backend.domain.models import Category, Dish, OrderItem, ShoppingCartItem, User


class UoW(ABC):
    """
    Unit of work pattern abstract.
    See repository for list of exceptions
    """

    user: Repository[User]
    dish: Repository[Dish]
    category: Repository[Category]
    shopping_cart: Repository[ShoppingCartItem]  # TODO: Make it aggregate
    order: Repository[Order]
    order_item: Repository[OrderItem]  # TODO: Delete and make aggregates

    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args) -> Self:
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
