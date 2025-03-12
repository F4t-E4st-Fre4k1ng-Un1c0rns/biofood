from typing import Annotated

from fastapi import APIRouter, Depends

from backend.domain.aggregates import OrderID
from backend.domain.value_objects import OrderStatus
from src.backend.application.push_subscription.subscribe import (
    PushSubscriptionInputDTO,
    PushSubscriptionOutputDTO,
)
from src.backend.ioc import IoC
from src.backend.presentation.dependencies import (
    AccessToken,
    provide_access_token,
)

push_router = APIRouter(prefix="")

@push_router.post(
    "/push",
    tags=["Push"],
    response_model=PushSubscriptionOutputDTO,
    summary="Create order with items from shopping cart",
)
async def create_subscription(
    ioc: Annotated[IoC, Depends()],
    access_token: Annotated[AccessToken, Depends(provide_access_token)],
    data: PushSubscriptionInputDTO,
):
    with ioc.subscribe_to_push(access_token) as subscribe_to_push_interactor:
        return await subscribe_to_push_interactor(data)
