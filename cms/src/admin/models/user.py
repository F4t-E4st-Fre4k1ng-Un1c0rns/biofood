from sqladmin import ModelView

from src.database.orm import UserORM

class UserAdmin(ModelView, model=UserORM):
    name = "Пользователь"
    name_plural = "Все пользователи"
    column_list = [UserORM.id, UserORM.role, UserORM.email]
