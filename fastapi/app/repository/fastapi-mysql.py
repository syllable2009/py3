# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import User, Base
import uvicorn
from di import injector, UserService
from dto import UserDTO
from pydantic import TypeAdapter
from typing import List
from dbmodel import Users
from sqlalchemy import delete, select, update, text

DATABASE_URL = "mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3"

# 创建数据库引擎，添加连接池配置
engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # 连接池的大小
    max_overflow=10,  # 连接池外的最大连接数
    pool_timeout=30,  # 获取连接的超时时间
    pool_recycle=1800  # 每1800秒回收连接
)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建 FastAPI 应用
app = FastAPI()


# @app.on_event("startup")
def on_startup():
    # 调用 create_all 创建所有表
    # Base.metadata.create_all(engine)
    # 如果只需要创建一个表
    # User.__table__.create(engine)
    print("application startup")


user_service = injector.get(UserService)
new_session = injector.get(Session)


# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 路由：创建用户
@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}


import json


# 路由：获取所有用户
@app.get("/users/")
def read_users():
    with new_session() as s:
        execute = s.execute(select(Users))
        execute_all: list[Users] = execute.all()
        print(execute_all)
        print(type(execute_all))
        ret = [
            user.dict()
            for user in execute_all
        ]
        return {"count": 100, "data": ret}
    return {}


# 路由：获取特定用户
@app.get("/users/{user_id}", response_model=Users)
def read_user(user_id: int):
    with new_session() as s:
        get = s.get(Users, user_id)
        print(get)
        print(type(get))
        return get


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
