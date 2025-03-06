import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv()

async_engine = create_async_engine(os.getenv("POSTGRES_DSN"))
async_session_maker = async_sessionmaker(async_engine)
