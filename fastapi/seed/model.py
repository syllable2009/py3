from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from typing import Optional
from contextlib import contextmanager

DATABASE_URL = "mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3?charset=utf8mb4"

engine = create_engine(DATABASE_URL, echo=True)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session


class Base(SQLModel, table=False):
    aid: int = Field(default=None, primary_key=True)
    uid: str = Field(default=None, index=True)
    content: Optional[str] = Field(default=None)
    create_time: Optional[datetime] = Field(default_factory=datetime.utcnow)
    update_time: Optional[datetime] = Field(default_factory=datetime.utcnow)

# 调用 create_all 创建所有表
# Base.metadata.create_all(engine)
# 如果只需要创建一个表
# User.__table__.create(engine)

class Test(Base, table=True):
    pass

# Test.__table__.create(engine)


