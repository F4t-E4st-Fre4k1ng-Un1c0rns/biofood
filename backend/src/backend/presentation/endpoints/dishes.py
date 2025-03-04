from typing import Annotated, Optional

from fastapi import APIRouter, Depends

from src.backend.application.get_dishes_list import (
    GetDishesListDTO,
    GetDishesListResultDTO,
)
from src.backend.domain.models import CategoryID
from src.backend.ioc import IoC

dishes_router = APIRouter(prefix="")


@dishes_router.get(
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
