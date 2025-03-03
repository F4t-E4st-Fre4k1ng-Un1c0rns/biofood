from collections.abc import Sequence

from pydantic import Field, RootModel

from backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import NotFound
from src.backend.domain.models import DishID, ShoppingCartItem


class ShoppingCartItemInputDTO(DomainModelBase):
    dish_id: DishID
    amount: int = Field(ge=1)


class DeleteFromShoppingCartItemsListDTO(RootModel):
    root: list["ShoppingCartItemInputDTO"]


class DeleteFromShoppingCartItemsListResultDTO(DomainModelBase):
    items: list[ShoppingCartItem]


class DeleteFromShoppingCartItemsList(
    Interactor[
        DeleteFromShoppingCartItemsListDTO, DeleteFromShoppingCartItemsListResultDTO
    ]
):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(
        self, data: DeleteFromShoppingCartItemsListDTO
    ) -> DeleteFromShoppingCartItemsListResultDTO:
        async with self.uow:
            for item in data.root:
                await self.__delete_from_cart(item)
            await self.uow.commit()
            result = await self.__get_shoppint_cart_items()
        return DeleteFromShoppingCartItemsListResultDTO(items=list(result))

    async def __delete_from_cart(self, item_input: ShoppingCartItemInputDTO):
        by_filter = {"user_id": self.token.user_id, "dish_id": item_input.dish_id}
        item = await self.uow.shopping_cart.find_one(by_filter=by_filter)

        new_amount = item.amount - item_input.amount
        if new_amount <= 0:
            return await self.uow.shopping_cart.delete_one(id=item.id)

        data = {"amount": new_amount}
        return await self.uow.shopping_cart.update_one(id=item.id, data=data)

    async def __get_shoppint_cart_items(self) -> Sequence[ShoppingCartItem]:
        by_filter = {"user_id": self.token.user_id}
        async with self.uow:
            return await self.uow.shopping_cart.find_many(by_filter=by_filter)
