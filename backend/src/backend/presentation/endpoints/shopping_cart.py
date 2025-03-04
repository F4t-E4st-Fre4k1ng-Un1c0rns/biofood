from typing import Annotated

from fastapi import APIRouter, Depends

from backend.application.shopping_cart.add_to_shopping_cart_items import (
    AddToShoppingCartItemsListDTO,
    AddToShoppingCartItemsListResultDTO,
)
from backend.application.shopping_cart.delete_from_shopping_cart_items import (
    DeleteFromShoppingCartItemsListDTO,
    DeleteFromShoppingCartItemsListResultDTO,
)
from src.backend.application.shopping_cart.get_shopping_cart_items_list import (
    GetShoppingCartItemsListResultDTO,
)
from src.backend.ioc import IoC
from src.backend.presentation.dependencies import AccessToken, provide_access_token

shopping_cart_router = APIRouter(prefix="")


@shopping_cart_router.get(
    "/shopping-cart-items",
    tags=["Store"],
    response_model=GetShoppingCartItemsListResultDTO,
    summary="Get current user's shopping cart items",
)
async def get_shopping_cart_items(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
):
    with ioc.get_shopping_cart_items_list(
        access_token
    ) as get_shopping_cart_items_list_interactor:
        return await get_shopping_cart_items_list_interactor()


@shopping_cart_router.put(
    "/shopping-cart-items",
    tags=["Store"],
    response_model=AddToShoppingCartItemsListResultDTO,
    summary="Add to existing or create new shopping cart items",
)
async def add_to_shopping_cart_items(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    data: AddToShoppingCartItemsListDTO,
):
    with ioc.add_to_shopping_cart_items_list(
        access_token
    ) as add_to_shopping_cart_items_list_interactor:
        return await add_to_shopping_cart_items_list_interactor(data)


@shopping_cart_router.delete(
    "/shopping-cart-items",
    tags=["Store"],
    response_model=DeleteFromShoppingCartItemsListResultDTO,
    summary="Delete from existing shopping cart items",
)
async def delete_from_shopping_cart_items(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    data: DeleteFromShoppingCartItemsListDTO,
):
    with ioc.delete_from_shopping_cart_items_list(
        access_token
    ) as delete_from_shopping_cart_items_list_interactor:
        return await delete_from_shopping_cart_items_list_interactor(data)
