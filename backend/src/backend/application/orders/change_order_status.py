from fastapi import BackgroundTasks
from pydantic import RootModel

from backend.application.common.orders_channel import OrdersChannel
from backend.application.common.push_service import PushService
from backend.domain.value_objects import OrderStatus, UserRole
from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order, OrderID
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import AuthorizationError


class ChangeOrderStatusDTO(DomainModelBase):
    id: OrderID
    new_status: OrderStatus


class ChangeOrderStatusResultDTO(RootModel):
    root: Order


class ChangeOrderStatus(Interactor[ChangeOrderStatusDTO, ChangeOrderStatusResultDTO]):
    def __init__(
        self,
        uow: UoW,
        orders_channel: OrdersChannel,
        push: PushService,
        token: AccessTokenI,
        background_tasks: BackgroundTasks,
    ):
        self.uow = uow
        self.token = token
        self.orders_channel = orders_channel
        self.push = push
        self.background_tasks = background_tasks

    async def __call__(self, data: ChangeOrderStatusDTO) -> ChangeOrderStatusResultDTO:
        if self.token.user_role == UserRole.client:
            raise AuthorizationError("You have no right to access all orders list")

        async with self.uow:
            order = await self.uow.order.update_one(
                data.id, {"status": data.new_status}
            )
            await self.orders_channel.publish_update(order)
            await self.uow.commit()

            if data.new_status in (OrderStatus.ready, OrderStatus.canceled):
                await self.__send_push_notification(order)

        return ChangeOrderStatusResultDTO(order)

    async def __send_push_notification(self, updated_order: Order):
        subscription_filters = {
            "user_id": updated_order.user_id,
        }
        subscriptions = await self.uow.push_subscription.find_many(subscription_filters)
        self.background_tasks.add_task(
            self.push.send, updated_order, list(subscriptions)
        )
