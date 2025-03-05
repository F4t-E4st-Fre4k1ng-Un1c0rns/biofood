from contextlib import contextmanager

from backend.application.common.authorization import AccessTokenI
from backend.application.orders.get_all_orders_for_today import GetAllOrdersForToday
from backend.application.orders.get_orders_by_id import GetOrderByID
from backend.application.shopping_cart.get_shopping_cart_items_list import (
    GetShoppingCartItemsList,
)
from src.backend.adapters.database.uow import UoWGateway
from src.backend.adapters.oauth import YandexIdGateway
from src.backend.application.authenticate import Authenticate
from src.backend.application.get_categories_list import GetCategoriesList
from src.backend.application.get_dishes_list import GetDishshesList
from src.backend.application.orders.create_order import CreateOrder
from src.backend.application.orders.get_orders_list import GetOrdersList
from src.backend.application.shopping_cart.add_to_shopping_cart_items import (
    AddToShoppingCartItemsList,
)
from src.backend.application.shopping_cart.delete_from_shopping_cart_items import (
    DeleteFromShoppingCartItemsList,
)
from src.backend.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    def __init__(self) -> None:
        self.uow_gateway = UoWGateway()
        self.yandex_id_gateway = YandexIdGateway()

    @contextmanager
    def authenticate(self):
        yield Authenticate(uow=self.uow_gateway, yandex_id=self.yandex_id_gateway)

    @contextmanager
    def get_categories_list(self):
        yield GetCategoriesList(uow=self.uow_gateway)

    @contextmanager
    def get_dishes_list(self):
        yield GetDishshesList(uow=self.uow_gateway)

    @contextmanager
    def get_shopping_cart_items_list(self, token: AccessTokenI):
        yield GetShoppingCartItemsList(uow=self.uow_gateway, token=token)

    @contextmanager
    def add_to_shopping_cart_items_list(self, token: AccessTokenI):
        yield AddToShoppingCartItemsList(uow=self.uow_gateway, token=token)

    @contextmanager
    def delete_from_shopping_cart_items_list(self, token: AccessTokenI):
        yield DeleteFromShoppingCartItemsList(uow=self.uow_gateway, token=token)

    @contextmanager
    def get_orders_list(self, token: AccessTokenI):
        yield GetOrdersList(uow=self.uow_gateway, token=token)

    @contextmanager
    def get_order_by_id(self, token: AccessTokenI):
        yield GetOrderByID(uow=self.uow_gateway, token=token)

    @contextmanager
    def create_order(self, token: AccessTokenI):
        yield CreateOrder(uow=self.uow_gateway, token=token)

    @contextmanager
    def get_all_orders_for_today(self, token: AccessTokenI):
        yield GetAllOrdersForToday(uow=self.uow_gateway, token=token)
