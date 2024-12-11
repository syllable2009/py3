from fastapi import FastAPI, Depends, Header, Cookie, HTTPException, Query, Request, Response, Form, \
    File, UploadFile
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# 异步
import asyncio
import uvicorn
import logging
from model import get_session, Test, engine
from sqlmodel import select, Session

from di import injector

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS中间件示例（可选）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from  testservice import TestService
user_service = injector.get(TestService)

@app.get("/", response_model=dict)
def read_root():
    # 路由处理函数返回一个字典，该字典将被 FastAPI 自动转换为 JSON 格式
    return {"Hello": "World"}


@app.post("/add/user/", response_model=Test)
def create_user(item: Test):
    with Session(engine) as s:
        print(item)  # 为什么add完成之后没有值了
        s.add(item)
        s.commit()
        print(item)
        return item


@app.get("/users/", response_model=list[Test])
def read_users():
    return user_service.get_all()


# q -- 是查询参数，指定为字符串类型或空（None）
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def update_item(item_id: int, item: dict):
    # 路由处理函数返回一个 Pydantic 模型实例，FastAPI 将自动将其转换为 JSON 格式，并作为响应发送给客户端
    item.id = item_id
    return item


@app.get("/header")
def header(user_agent: str = Header(None), session_token: str = Cookie(None)):
    # 使用 Header 和 Cookie 类型注解获取请求头和 Cookie 数据。
    return {"User-Agent": user_agent, "Session-Token": session_token}


@app.get("/redirect")
def redirect():
    # 使用 RedirectResponse 实现重定向，将客户端重定向到 /items/ 路由
    return RedirectResponse(url="/items/333")


@app.get("/error")
def error(item_id: int):
    # 使用 HTTPException 抛出异常，返回自定义的状态码和详细信息。
    raise HTTPException(status_code=item_id, detail="Item not found")
    return {"item_id": item_id}


@app.get("/self")
def self(item_id: int = 999):
    content = {"item_id": item_id}
    headers = {"X-Custom-Header": "custom-header-value"}
    # 使用 JSONResponse 自定义响应头
    return JSONResponse(content=content, headers=headers)


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


# 路由操作函数
@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
