from abc import abstractmethod

from src.backend.domain.aggregates import Order
from src.backend.domain.models import PushSubscription


class Push:
    @abstractmethod
    async def send(self, updated_order: Order, subscriptions: list[PushSubscription]):
        raise NotImplementedError
