from backend.domain.value_objects import UserRole
from pydantic import RootModel

from src.backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.aggregates import Order, OrderID
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import AuthorizationError


class GetOrderByIdDTO(DomainModelBase):
    id: OrderID


class GetOrderByIdResultDTO(RootModel):
    root: Order


class GetOrderByID(Interactor[GetOrderByIdDTO, GetOrderByIdResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data: GetOrderByIdDTO) -> GetOrderByIdResultDTO:
        async with self.uow:
            by_filter = {"id": data.id}
            order = await self.uow.order.find_one(by_filter=by_filter)
            if order.user_id.hex != self.token.user_id and self.token.user_role == UserRole.client:
                raise AuthorizationError("You have no right to access this order")
            return GetOrderByIdResultDTO(order)
