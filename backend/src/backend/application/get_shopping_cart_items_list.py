from backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.models import ShoppingCartItem


class GetShoppingCartItemsListResultDTO(DomainModelBase):
    items: list[ShoppingCartItem]


class GetShoppingCartItemsList(Interactor[None, GetShoppingCartItemsListResultDTO]):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(self, data=None) -> GetShoppingCartItemsListResultDTO:
        by_filter = {"user_id": self.token.user_id}
        async with self.uow:
            shopping_cart_items = await self.uow.shopping_cart.find_many(
                by_filter=by_filter
            )
        return GetShoppingCartItemsListResultDTO(items=list(shopping_cart_items))
