from typing import Annotated, Optional

from fastapi import APIRouter, Depends

from backend.application.add_to_shopping_cart_items import (
    AddToShoppingCartItemsListDTO,
    AddToShoppingCartItemsListResultDTO,
)
from backend.application.delete_from_shopping_cart_items import (
    DeleteFromShoppingCartItemsListDTO,
    DeleteFromShoppingCartItemsListResultDTO,
)
from src.backend.application.authenticate import (
    AuthenticateDTO,
    AuthenticateResultDTO,
)
from src.backend.application.create_order import CreateOrderDTO, CreateOrderResultDTO
from src.backend.application.get_categories_list import GetCategoriesListResultDTO
from src.backend.application.get_dishes_list import (
    GetDishesListDTO,
    GetDishesListResultDTO,
)
from src.backend.application.get_orders_list import GetOrdersListResultDTO
from src.backend.application.get_shopping_cart_items_list import (
    GetShoppingCartItemsListResultDTO,
)
from src.backend.domain.models import CategoryID
from src.backend.ioc import IoC
from src.backend.presentation.dependencies import AccessToken, provide_access_token

api_router = APIRouter(prefix="/api")


@api_router.post(
    "/authenticate",
    tags=["Auth"],
    response_model=AuthenticateResultDTO,
    summary="Authenticate by OAouth token",
)
async def authenticate(ioc: Annotated[IoC, Depends()], data: AuthenticateDTO):
    with ioc.authenticate() as authenticate_interactor:
        return await authenticate_interactor(data)


@api_router.get(
    "/categories",
    tags=["Store"],
    response_model=GetCategoriesListResultDTO,
    summary="Get categories of all dishes",
)
async def get_categories_list(
    ioc: Annotated[IoC, Depends()],
):
    with ioc.get_categories_list() as get_categories_list_interactor:
        data = await get_categories_list_interactor()
        return data


@api_router.get(
    "/dishes",
    tags=["Store"],
    response_model=GetDishesListResultDTO,
    summary="Get all dishes filtered by category",
)
async def get_dishes_list(
    ioc: Annotated[IoC, Depends()],
    category_id: Optional[CategoryID] = None,
):
    with ioc.get_dishes_list() as get_dishes_list_interactor:
        return await get_dishes_list_interactor(
            GetDishesListDTO(category_id=category_id)
        )


@api_router.get(
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


@api_router.put(
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


@api_router.delete(
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


@api_router.get(
    "/orders",
    tags=["Store"],
    response_model=GetOrdersListResultDTO,
    summary="Get list of users orders",
)
async def get_orders_list(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
):
    with ioc.get_orders_list(access_token) as get_orders_list_interactor:
        return await get_orders_list_interactor()


@api_router.post(
    "/orders",
    tags=["Store"],
    response_model=CreateOrderResultDTO,
    summary="Create order with items from shopping cart",
)
async def create_order(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    data: CreateOrderDTO,
):
    with ioc.create_order(access_token) as create_order_interactor:
        return await create_order_interactor(data)
