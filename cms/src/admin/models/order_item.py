from sqladmin import ModelView

from src.database.orm import OrderItemORM

class OrderItemAdmin(ModelView, model=OrderItemORM):
    name = "Предмет заказа"
    name_plural = "Все предметы заказов"
    column_list = [OrderItemORM.id, OrderItemORM.order, OrderItemORM.dish, OrderItemORM.amount]
