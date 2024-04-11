import configparser

config = configparser.ConfigParser()
config.read('db.config.ini')

host = config.get('database', 'host')
port = config.getint('database', 'port')
username = config.get('database', 'username')
password = config.get('database', 'password')
database = config.get('database', 'database')

print(f"host: {host}")
print(f"port: {port}")
print(f"username: {username}")
print(f"password: {password}")
print(f"database: {database}")

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
# import os
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = 'mysql+pymysql://'
# SQLAlchemy
engine = create_engine(DATABASE_URL,echo=True,pool_size=5,pool_recycle=3600)
from sqlalchemy.sql import func
metadata = MetaData()
follow_event = Table(
    "recommend_follow_event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("login_id", String(50)),
    Column("type", String(50)),
    Column("create_time", DateTime, default=func.now(), nullable=False),
)



#
def query_by_id(id:int):
    return follow_event.select().where(1 == follow_event.c.id)
#
# from databases import Database
# db = Database(DATABASE_URL)
# one = db.fetch_one(query=query)
# print(one)


# import asyncio
# import databases
#
# async def database_basic():
#     database = databases(url="mysql://")
#     await database.connect()
#     sql = "select * from recommend_follow_event where id = 1;"
#     result = await database.fetch_all(query=sql)
#     print(result)

from sqlalchemy.orm import sessionmaker,declarative_base
DbSession = sessionmaker(bind=engine)
session = DbSession()

Base = declarative_base()

class Event(Base):
    __tablename__ = "recommend_follow_event"
    id = Column(Integer, primary_key=True)
    loginId = Column("login_id", String(50))
    type = type(String)
    createTime = Column("create_time", DateTime, default=func.now(), nullable=False)


from sqlalchemy import select
if __name__ == '__main__':
    by_id = query_by_id(1)
    one = session.query(follow_event).filter_by(id=1).one()
    print(type(one))
    print(one.create_time)
    import sqlalchemy
    print(sqlalchemy.__version__)
    stmt = select(Event).where(Event.id == 1)
    print(type(stmt))
    patrick = session.scalars(stmt).one()
    print(type(patrick))
    print(patrick.loginId)







