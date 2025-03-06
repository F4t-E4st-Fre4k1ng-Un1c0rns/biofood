from sqladmin import ModelView

from src.database.orm import OrderORM

class OrderAdmin(ModelView, model=OrderORM):
    name = "Заказ"
    name_plural = "Все заказы"
    column_list = [OrderORM.id, OrderORM.user, OrderORM.status, OrderORM.created_at, OrderORM.updated_at, OrderORM.takeout_time]
