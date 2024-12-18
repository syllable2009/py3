import os
DATABASE_URL = os.getenv("DATABASE_URL")
from sqlalchemy import create_engine

# SQLAlchemy
engine_url = create_engine(DATABASE_URL)

engine = create_engine(engine_url)





