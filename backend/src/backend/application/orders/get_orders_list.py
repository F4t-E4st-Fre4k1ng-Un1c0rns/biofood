from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order
from src.backend.domain.common import Base as DomainModelBase


class GetOrdersListResultDTO(DomainModelBase):
    items: list[Order]


class GetOrdersList(Interactor[None, GetOrdersListResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data: None = None) -> GetOrdersListResultDTO:
        async with self.uow:
            by_filter = {"user_id": self.token.user_id}
            orders_list = await self.uow.order.find_many(by_filter=by_filter)
            return GetOrdersListResultDTO(items=list(orders_list))
