import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv()

engine = create_async_engine(os.getenv("POSTGRES_DSN"))
session_maker = async_sessionmaker(engine)

engine_analyze = create_async_engine(os.getenv("POSTGRES_DSN_ANALYZE"))
session_maker_analyze = async_sessionmaker(engine_analyze)
