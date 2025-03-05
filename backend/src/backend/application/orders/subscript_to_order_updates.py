from backend.domain.value_objects import UserRole
from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import AuthorizationError


class GetOrdersListResultDTO(DomainModelBase):
    items: list[Order]


# VALIDATE TOKEN IN DEPS
class GetOrdersList(Interactor[None, GetOrdersListResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data: None = None) -> GetOrdersListResultDTO:
        in_range_filter = {}
        async with self.uow:
            orders_list = await self.uow.order.find_many(in_range_filter=in_range_filter)
            return GetOrdersListResultDTO(items=list(orders_list))

