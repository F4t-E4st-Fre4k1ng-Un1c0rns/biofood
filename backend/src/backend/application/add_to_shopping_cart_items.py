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


class AddToShoppingCartItemsListDTO(RootModel):
    root: list["ShoppingCartItemInputDTO"]


class AddToShoppingCartItemsListResultDTO(DomainModelBase):
    items: list[ShoppingCartItem]


class AddToShoppingCartItemsList(
    Interactor[AddToShoppingCartItemsListDTO, AddToShoppingCartItemsListResultDTO]
):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(
        self, data: AddToShoppingCartItemsListDTO
    ) -> AddToShoppingCartItemsListResultDTO:
        async with self.uow:
            for item in data.root:
                await self.__add_to_cart(item)
            await self.uow.commit()
            result = await self.__get_shoppint_cart_items()
        return AddToShoppingCartItemsListResultDTO(items=list(result))

    async def __add_to_cart(self, item_input: ShoppingCartItemInputDTO):
        try:
            item = await self.__update_cart_item_amount(item_input)
        except NotFound:
            item = await self.__create_cart_item(item_input)
        return item

    async def __update_cart_item_amount(
        self, item_input: ShoppingCartItemInputDTO
    ) -> ShoppingCartItem:
        by_filter = {"user_id": self.token.user_id, "dish_id": item_input.dish_id}
        item = await self.uow.shopping_cart.find_one(by_filter=by_filter)

        data = {"amount": item.amount + item_input.amount}
        return await self.uow.shopping_cart.update_one(id=item.id, data=data)

    async def __create_cart_item(
        self, item_input: ShoppingCartItemInputDTO
    ) -> ShoppingCartItem:
        item_data = {
            "user_id": self.token.user_id,
            "dish_id": item_input.dish_id,
            "amount": item_input.amount,
        }
        return await self.uow.shopping_cart.create_one(item_data)

    async def __get_shoppint_cart_items(self) -> Sequence[ShoppingCartItem]:
        by_filter = {"user_id": self.token.user_id}
        async with self.uow:
            return await self.uow.shopping_cart.find_many(by_filter=by_filter)
