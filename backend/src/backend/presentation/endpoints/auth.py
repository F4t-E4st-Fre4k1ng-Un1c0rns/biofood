from typing import Annotated

from fastapi import APIRouter, Depends

from backend.domain.aggregates import OrderID
from src.backend.application.authenticate import (
    AuthenticateDTO,
    AuthenticateResultDTO,
)
from src.backend.ioc import IoC


auth_router = APIRouter(prefix="")


@auth_router.post(
    "/authenticate",
    tags=["Auth"],
    response_model=AuthenticateResultDTO,
    summary="Authenticate by OAouth token",
)
async def authenticate(ioc: Annotated[IoC, Depends()], data: AuthenticateDTO):
    with ioc.authenticate() as authenticate_interactor:
        return await authenticate_interactor(data)


