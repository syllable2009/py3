from sqlmodel import Field,Session,SQLModel,create_engine,select
from typing import Optional
from fastapi import FastAPI
import uvicorn

class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None)
    fullname: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)


engine = create_engine("mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3?charset=utf8mb4")

# 创建 FastAPI 应用
app = FastAPI()

# 路由：获取所有用户
@app.get("/users/", response_model=list[Users])
def read_users():
    with Session(engine) as s:
        execute = s.exec(select(Users))
        execute_all: list[Users] = execute.all()
        print(execute_all)
        print(type(execute_all))
        return execute_all
    return []

@app.get("/users/page", response_model=dict)
def read_users_page():
    with Session(engine) as s:
        execute = s.exec(select(Users))
        execute_all: list[Users] = execute.all()
        print(execute_all)
        print(type(execute_all))
        return {"count":100,"data":execute_all}
    return {}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
