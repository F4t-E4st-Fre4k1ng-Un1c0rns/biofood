from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.application.orders.change_order_status import (
    ChangeOrderStatusDTO,
    ChangeOrderStatusResultDTO,
)
from backend.application.orders.subscribe_to_all_orders import (
    SubscribeToAllOrdersResultDTO,
)
from backend.domain.aggregates import OrderID
from backend.domain.value_objects import OrderStatus
from src.backend.application.orders.create_order import (
    CreateOrderDTO,
    CreateOrderResultDTO,
)
from src.backend.application.orders.subscribe_to_orders_list import (
    SubscribeOrdersListResultDTO,
)
from src.backend.ioc import IoC
from src.backend.presentation.dependencies import (
    AccessToken,
    provide_access_token,
    provide_admin_access_token,
)

orders_router = APIRouter(prefix="")


@orders_router.get(
    "/orders",
    tags=["Store"],
    response_model=SubscribeOrdersListResultDTO,
    summary="Subscribe to users orders changes",
)
async def get_orders_list(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
):
    with ioc.subscribe_to_orders_list(access_token) as subscribe_to_orders_generator:

        async def string_generator():
            async for item in subscribe_to_orders_generator():
                yield "".join(("data:", item.model_dump_json(), "\n\n"))

        return StreamingResponse(string_generator(), media_type="text/event-stream")


@orders_router.get(
    "/orders/all",
    tags=["Staff"],
    response_model=SubscribeToAllOrdersResultDTO,
    summary="Subsribe to all orders changes",
)
async def get(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_admin_access_token)],
):
    with ioc.subscribe_to_all_orders(access_token) as subscribe_to_orders_generator:

        async def string_generator():
            async for item in subscribe_to_orders_generator():
                yield "".join(("data:", item.model_dump_json(), "\n\n"))

        return StreamingResponse(string_generator(), media_type="text/event-stream")


class ChangeOrderStatusInput(BaseModel):
    status: OrderStatus


@orders_router.patch(
    "/orders/{id}",
    tags=["Staff"],
    response_model=ChangeOrderStatusResultDTO,
    summary="Change order status",
)
async def change_order_status(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    id: OrderID,
    data: ChangeOrderStatusInput,
    background_tasks: BackgroundTasks
):
    with ioc.change_order_status(access_token, background_tasks) as change_order_status_interactor:
        return await change_order_status_interactor(
            ChangeOrderStatusDTO(id=id, new_status=data.status)
        )


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
