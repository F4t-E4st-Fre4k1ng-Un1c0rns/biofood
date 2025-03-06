from sqladmin import ModelView

from src.database.orm import ShoppingCartItemORM

class ShoppingCartItemAdmin(ModelView, model=ShoppingCartItemORM):
    name = "Предмет корзины пользователя"
    name_plural = "Все предметы корзин пользователей"

    column_list = [ShoppingCartItemORM.id, ShoppingCartItemORM.user, ShoppingCartItemORM.dish, ShoppingCartItemORM.amount]
