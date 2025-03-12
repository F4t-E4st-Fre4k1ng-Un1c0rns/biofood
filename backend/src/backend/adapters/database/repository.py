from abc import abstractmethod
from operator import or_
from typing import Any, Iterable, Sequence
from uuid import UUID

from sqlalchemy import Select, delete, func, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.adapters.database.orm.orm import (
    CategoryORM,
    DishORM,
    OrderItemORM,
    OrderORM,
    ShoppingCartItemORM,
    PushSubscriptionORM,
    UserORM,
)
from src.backend.application.common.dto import (
    ByFilter,
    InFilter,
    InRangeFilter,
    ModelData,
    NotNullFilter,
    Pagination,
    SearchFilter,
    Sorting,
    SortingDirection,
)
from src.backend.application.common.repository import Repository
from src.backend.application.common.sentinel import _sentinel
from src.backend.domain.aggregates import Order
from src.backend.domain.exceptions import IntegrityCompromised, NotFound
from src.backend.domain.models import Category, Dish, OrderItem, ShoppingCartItem, PushSubscription, User


class SQLAlchemyRepository[ModelT](Repository[ModelT]):
    model: Any

    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def _map_to_domain_model(self, orm_model) -> ModelT:
        raise NotImplementedError

    async def _bulk_map_to_domain_model(self, orm_models: Iterable) -> Sequence[ModelT]:
        return [await self._map_to_domain_model(orm) for orm in orm_models]

    def __add_filtration(
        self,
        stmt: Select,
        by_filter: ByFilter,
        in_filter: InFilter,
        in_range_filter: InRangeFilter,
        not_null_filter: NotNullFilter,
        search_filter: SearchFilter,
    ) -> Select:
        if by_filter is not _sentinel:
            stmt = stmt.filter_by(**by_filter)

        if in_filter is not _sentinel:
            for field in in_filter:
                stmt = stmt.filter(getattr(self.model, field).in_(in_filter[field]))

        if in_range_filter is not _sentinel:
            for field in in_range_filter:
                stmt = stmt.filter(
                    getattr(self.model, field).between(*in_range_filter[field])
                )

        if not_null_filter is not _sentinel:
            for field in not_null_filter:
                stmt = stmt.filter(getattr(self.model, field).is_not(None))

        if search_filter is not _sentinel:
            stmt = stmt.filter(
                or_(
                    *[
                        getattr(self.model, field).ilike(f"%{search_filter[field]}%")
                        for field in search_filter
                    ]
                )
            )

        return stmt

    def __add_ordering(
        self,
        stmt: Select,
        sorting: Sorting,
    ) -> Select:
        if sorting is not _sentinel:
            for field in sorting:
                stmt = (
                    stmt.order_by(getattr(self.model, field))
                    if sorting is SortingDirection.ascending
                    else stmt.order_by(getattr(self.model, field).desc())
                )
        return stmt

    def __add_pagination(self, stmt: Select, pagination: Pagination) -> Select:
        if pagination is not _sentinel:
            stmt = stmt.limit(pagination.limit)
            stmt = stmt.offset((pagination.page - 1) * pagination.limit)
        return stmt

    async def create_one(self, data: ModelData) -> ModelT:
        stmt = insert(self.model).values(**data).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            return await self._map_to_domain_model(res.scalar_one())
        except IntegrityError:
            raise IntegrityCompromised

    async def create_many(self, data: Iterable[ModelData]) -> Sequence[ModelT]:
        return [await self.create_one(obj) for obj in data]

    async def update_one(self, id: UUID, data: ModelData) -> ModelT:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            return await self._map_to_domain_model(res.scalar_one())
        except IntegrityError:
            raise IntegrityCompromised
        except NoResultFound:
            raise NotFound

    async def update_many(
        self, ids: Iterable[UUID], data: Iterable[ModelData]
    ) -> Sequence[ModelT]:
        return [await self.update_one(id, obj) for id, obj in zip(ids, data)]

    async def delete_one(self, id: UUID) -> None:
        stmt = delete(self.model).filter_by(id=id)
        try:
            await self.session.execute(stmt)
        except IntegrityError:
            raise IntegrityCompromised

    async def delete_many(self, ids: Iterable[UUID]) -> None:
        for id in ids:
            await self.delete_one(id)

    async def find_one(
        self,
        by_filter: ByFilter = _sentinel,
        in_filter: InFilter = _sentinel,
        in_range_filter: InRangeFilter = _sentinel,
        not_null_filter: NotNullFilter = _sentinel,
        search_filter: SearchFilter = _sentinel,
        sorting: Sorting = _sentinel,
    ) -> ModelT:
        stmt = select(self.model)
        stmt = self.__add_filtration(
            stmt,
            by_filter=by_filter,
            in_filter=in_filter,
            in_range_filter=in_range_filter,
            not_null_filter=not_null_filter,
            search_filter=search_filter,
        )
        stmt = self.__add_ordering(stmt, sorting)

        try:
            res = await self.session.execute(stmt)
            return await self._map_to_domain_model(res.scalar_one())
        except NoResultFound:
            raise NotFound

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
        stmt = select(self.model)
        stmt = self.__add_filtration(
            stmt,
            by_filter=by_filter,
            in_filter=in_filter,
            in_range_filter=in_range_filter,
            not_null_filter=not_null_filter,
            search_filter=search_filter,
        )
        stmt = self.__add_ordering(stmt, sorting)
        stmt = self.__add_pagination(stmt, pagination)

        res = await self.session.execute(stmt)

        return await self._bulk_map_to_domain_model(res.scalars().fetchall())

    async def count(
        self,
        by_filter: ByFilter = _sentinel,
        in_filter: InFilter = _sentinel,
        in_range_filter: InRangeFilter = _sentinel,
        search_filter: SearchFilter = _sentinel,
        not_null_filter: NotNullFilter = _sentinel,
    ) -> int:
        stmt = select(func.count()).select_from(self.model)
        stmt = self.__add_filtration(
            stmt,
            by_filter=by_filter,
            in_filter=in_filter,
            in_range_filter=in_range_filter,
            not_null_filter=not_null_filter,
            search_filter=search_filter,
        )
        res = await self.session.execute(stmt)
        return res.scalar_one()


class UserRepository(SQLAlchemyRepository[User]):
    model = UserORM

    async def _map_to_domain_model(self, orm_model) -> User:
        return User.model_validate(orm_model)


class CategoryRepository(SQLAlchemyRepository[Category]):
    model = CategoryORM

    async def _map_to_domain_model(self, orm_model) -> Category:
        return Category.model_validate(orm_model)


class DishRepository(SQLAlchemyRepository[Dish]):
    model = DishORM

    async def _map_to_domain_model(self, orm_model) -> Dish:
        return Dish.model_validate(orm_model)


# TODO: Make it aggregate
class ShoppingCartItemRepository(SQLAlchemyRepository[ShoppingCartItem]):
    model = ShoppingCartItemORM

    async def _map_to_domain_model(self, orm_model) -> ShoppingCartItem:
        return ShoppingCartItem.model_validate(orm_model)


class OrderRepository(SQLAlchemyRepository[Order]):
    model = OrderORM

    async def _map_to_domain_model(self, orm_model) -> Order:
        return Order.model_validate(orm_model)


class PushSubscriptionRepository(SQLAlchemyRepository[PushSubscriptionORM]):
    model = PushSubscriptionORM

    async def _map_to_domain_model(self, orm_model) -> Order:
        return PushSubscription.model_validate(orm_model)


# TODO: DELETE And make aggregates
class OrderItemRepository(SQLAlchemyRepository[OrderItem]):
    model = OrderItemORM

    async def _map_to_domain_model(self, orm_model) -> OrderItem:
        return OrderItem.model_validate(orm_model)
