from typing import Annotated

from fastapi import APIRouter, Depends

from src.backend.application.get_categories_list import GetCategoriesListResultDTO
from src.backend.ioc import IoC

categories_router = APIRouter(prefix="")


@categories_router.get(
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
