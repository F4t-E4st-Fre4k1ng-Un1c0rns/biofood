from typing import Optional

from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.models import CategoryID, Dish


class GetDishesListDTO(DomainModelBase):
    category_id: Optional[CategoryID]


class GetDishesListResultDTO(DomainModelBase):
    items: list[Dish]


class GetDishshesList(Interactor[GetDishesListDTO, GetDishesListResultDTO]):
    def __init__(self, uow: UoW):
        self.uow = uow

    async def __call__(self, data: GetDishesListDTO) -> GetDishesListResultDTO:
        if data.category_id is not None:
            by_filter = {"category_id": data.category_id}
        else:
            by_filter = {}

        async with self.uow as uow:
            dishes = await uow.dish.find_many(by_filter=by_filter)
        return GetDishesListResultDTO(items=list(dishes))
