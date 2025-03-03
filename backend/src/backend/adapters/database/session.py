from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.backend.settings import settings

engine = create_async_engine(str(settings.POSTGRES_DSN))
session_factory = async_sessionmaker(engine, expire_on_commit=False)
