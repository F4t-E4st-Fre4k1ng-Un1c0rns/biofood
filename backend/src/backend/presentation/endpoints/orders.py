from typing import Annotated

from fastapi import APIRouter, Depends

from backend.application.orders.get_orders_by_id import (
    GetOrderByIdDTO,
    GetOrderByIdResultDTO,
)
from backend.domain.aggregates import OrderID
from src.backend.application.orders.create_order import (
    CreateOrderDTO,
    CreateOrderResultDTO,
)
from src.backend.application.orders.get_orders_list import GetOrdersListResultDTO
from src.backend.ioc import IoC
from src.backend.presentation.dependencies import AccessToken, provide_access_token

orders_router = APIRouter(prefix="")


@orders_router.get(
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


@orders_router.get(
    "/orders/{id}",
    tags=["Store"],
    response_model=GetOrderByIdResultDTO,
    summary="Get users order by id",
)
async def get_order_by_id(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    id: OrderID,
):
    with ioc.get_order_by_id(access_token) as get_order_by_id_interactor:
        return await get_order_by_id_interactor(GetOrderByIdDTO(id=id))


@orders_router.post(
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
