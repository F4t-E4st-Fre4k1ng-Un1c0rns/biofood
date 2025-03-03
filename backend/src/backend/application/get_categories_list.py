from backend.domain.common import Base as PydanticBase
from backend.domain.models import Category

from .common.interactor import Interactor
from .common.uow import UoW


class GetCategoriesListResultDTO(PydanticBase):
    items: list[Category]


class GetCategoriesList(Interactor[None, GetCategoriesListResultDTO]):
    def __init__(self, uow: UoW):
        self.uow = uow

    async def __call__(self, data: None = None) -> GetCategoriesListResultDTO:
        async with self.uow as uow:
            categories = await uow.category.find_many()
        return GetCategoriesListResultDTO(items=list(categories))
