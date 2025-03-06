from fastapi import FastAPI
from sqladmin import Admin

from src.database.session import async_engine
from src.admin import authentication_backend, models

app = FastAPI(title="Biofood CMS")
admin = Admin(app=app, engine=async_engine, authentication_backend=authentication_backend)
for model in models:
    admin.add_view(model)