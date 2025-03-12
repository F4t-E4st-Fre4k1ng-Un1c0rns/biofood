from backend.application.common.uow import UoW

from .repository import (
    CategoryRepository,
    DishRepository,
    OrderItemRepository,
    OrderRepository,
    ShoppingCartItemRepository,
    PushSubscriptionRepository,
    UserRepository,
)
from .session import session_factory


class UoWGateway(UoW):
    def __init__(self, session_factory=session_factory) -> None:
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)
        self.push_subscription = PushSubscriptionRepository(self.session)
        self.dish = DishRepository(self.session)
        self.category = CategoryRepository(self.session)
        self.shopping_cart = ShoppingCartItemRepository(self.session)
        self.order = OrderRepository(self.session)
        self.order_item = OrderItemRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
