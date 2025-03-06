from sqladmin import ModelView

from src.database.orm import DishORM

class DishAdmin(ModelView, model=DishORM):
    name = "Блюдо"
    name_plural = "Все блюда"
    column_list = [DishORM.id, DishORM.category, DishORM.name, DishORM.price, DishORM.weight]
