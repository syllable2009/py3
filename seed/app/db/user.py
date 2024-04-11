from .base import BaseDB
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class User(BaseDB):
    __tablename__ = "recommend_follow_event"
    id = Column(Integer, primary_key=True)
    loginId = Column("login_id", String(50))
    type = type(String)
    createTime = Column("create_time", DateTime, default=func.now(), nullable=False)



