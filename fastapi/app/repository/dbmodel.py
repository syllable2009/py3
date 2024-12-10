from sqlmodel import Field, SQLModel, DateTime
from sqlmodel import create_engine, SQLModel
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None)
    fullname: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    # create_time: datetime = Field(default_factory=datetime.now)
    # update_time: datetime = Field(default_factory=datetime.now)


from di import injector, UserService
from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update, text

if __name__ == "__main__":
    print(Users.__table__)  # 打印表结构
    new_session = injector.get(Session)
    with new_session as s:
        stmt = select(Users)
        execute = s.execute(stmt)
        print(execute.all())
