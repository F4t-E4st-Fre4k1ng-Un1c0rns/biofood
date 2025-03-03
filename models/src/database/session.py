import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv("POSTGRES_DSN"))
session_maker = sessionmaker(engine)

engine_analyze = create_engine(os.getenv("POSTGRES_DSN_ANALYZE"))
session_maker_analyze = sessionmaker(engine_analyze)
