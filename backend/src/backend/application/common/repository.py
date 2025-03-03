from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Iterable, Sequence, TypeVar
from uuid import UUID

from .dto import (
    ByFilter,
    InFilter,
    InRangeFilter,
    ModelData,
    NotNullFilter,
    Pagination,
    SearchFilter,
    Sorting,
)
from .sentinel import _sentinel

ModelT = TypeVar("ModelT")


class Repository[ModelT](ABC):
    """
    Abstract of repository pattern on Unit of work

    Raises:
    NotFound: If specific ModelT wasn't found. e.g. when finding one
    InetrityCompromised: If inserted data refers to not existing objects

    """

    @abstractmethod
    async def create_one(self, data: ModelData) -> ModelT:
        raise NotImplementedError

    @abstractmethod
    async def create_many(self, data: Iterable[ModelData]) -> Sequence[ModelT]:
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, id: UUID, data: ModelData) -> ModelT:
        raise NotImplementedError

    @abstractmethod
    async def update_many(
        self, ids: Iterable[UUID], data: Sequence[ModelData]
    ) -> Sequence[ModelT]:
        raise NotImplementedError

    async def delete_one(self, id: UUID) -> None:
        raise NotImplementedError

    async def delete_many(self, ids: Iterable[UUID]) -> None:
        raise NotImplementedError

    @abstractmethod
    async def find_one(
        self,
        by_filter: ByFilter = _sentinel,
        in_filter: InFilter = _sentinel,
        in_range_filter: InRangeFilter = _sentinel,
        not_null_filter: NotNullFilter = _sentinel,
        search_filter: SearchFilter = _sentinel,
        sorting: Sorting = _sentinel,
    ) -> ModelT:
        raise NotImplementedError

    @abstractmethod
    async def find_many(
        self,
        by_filter: ByFilter = _sentinel,
        in_filter: InFilter = _sentinel,
        in_range_filter: InRangeFilter = _sentinel,
        not_null_filter: NotNullFilter = _sentinel,
        search_filter: SearchFilter = _sentinel,
        sorting: Sorting = _sentinel,
        pagination: Pagination = _sentinel,
    ) -> Sequence[ModelT]:
        raise NotImplementedError

    @abstractmethod
    async def count(
        self,
        by_filter: ByFilter = _sentinel,
        in_filter: InFilter = _sentinel,
        in_range_filter: InRangeFilter = _sentinel,
        search_filter: SearchFilter = _sentinel,
        not_null_filter: NotNullFilter = _sentinel,
    ) -> int:
        raise NotImplementedError
