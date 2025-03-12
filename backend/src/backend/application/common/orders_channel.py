from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator

from redis.asyncio.client import PubSub

from src.backend.domain.aggregates import Order


class OrdersChannel(ABC):
    """
    Reidis channel with orders updates
    """

    @abstractmethod
    async def publish_update(self, updated_order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    def generate_updates(self) -> AsyncGenerator[Order]:
        raise NotImplementedError
