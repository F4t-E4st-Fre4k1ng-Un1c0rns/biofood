from sqladmin import ModelView

from src.database.orm import CategoryORM

class CategoryAdmin(ModelView, model=CategoryORM):
    name = "Категория"
    name_plural = "Все категории"
    column_list = [CategoryORM.id, CategoryORM.name]
