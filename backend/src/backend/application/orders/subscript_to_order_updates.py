from datetime import timedelta, timezone
from dateutil.utils import today

from backend.application.common.dto import InRangeFilter
from backend.domain.value_objects import UserRole
from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import AuthorizationError


class GetOrdersListResultDTO(DomainModelBase):
    items: list[Order]


class GetAllOrdersForTodayList(Interactor[None, GetOrdersListResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data: None = None) -> GetOrdersListResultDTO:
        if self.token.user_role == UserRole.client:
            raise AuthorizationError("You have no right to access all orders list")
        in_range_filter: InRangeFilter = {
            "created_at": (today(timezone.utc), today(timezone.utc) + timedelta(days=1))
        }
        async with self.uow:
            orders_list = await self.uow.order.find_many(
                in_range_filter=in_range_filter
            )
            return GetOrdersListResultDTO(items=list(orders_list))
