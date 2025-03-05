from datetime import datetime
from typing import Optional

from pydantic import AwareDatetime

from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order, OrderID
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.models import ShoppingCartItem, UserID
from src.backend.domain.value_objects import OrderStatus


class CreateOrderDTO(DomainModelBase):
    takeout_time: Optional[AwareDatetime]


class CreateOrderResultDTO(DomainModelBase):
    items: list[Order]


class CreateOrder(Interactor[CreateOrderDTO, CreateOrderResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data: CreateOrderDTO) -> CreateOrderResultDTO:
        async with self.uow:
            await self.__get_users_shopping_cart_items()
            order = await self.__create_order(data.takeout_time)
            await self.__add_items_from_shopping_cart_to_order(order.id)
            await self.__clear_shopping_cart()
            await self.uow.commit()
            orders_list = await self.uow.order.find_many(
                by_filter={"user_id": self.token.user_id}
            )
            return CreateOrderResultDTO(items=list(orders_list))

    async def __get_users_shopping_cart_items(self) -> list[ShoppingCartItem]:
        by_filter = {"user_id": self.token.user_id}
        async with self.uow:
            shopping_cart_items = await self.uow.shopping_cart.find_many(
                by_filter=by_filter
            )
        return list(shopping_cart_items)

    async def __create_order(self, takeout_time: datetime | None):
        data = {
            "user_id": self.token.user_id,
            "status": OrderStatus.pending,
            "takeout_time": takeout_time,
        }
        return await self.uow.order.create_one(data)

    async def __add_items_from_shopping_cart_to_order(self, order_id: OrderID):
        items = await self.uow.shopping_cart.find_many(
            by_filter={"user_id": self.token.user_id}
        )
        for item in items:
            data = {
                "order_id": order_id,
                "dish_id": item.dish.id,
                "amount": item.amount,
            }
            await self.uow.order_item.create_one(data=data)

    async def __clear_shopping_cart(self):
        by_filter = {"user_id": self.token.user_id}
        items = await self.uow.shopping_cart.find_many(by_filter=by_filter)
        await self.uow.shopping_cart.delete_many((i.id for i in items))
