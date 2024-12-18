from fastapi import FastAPI, Depends, Header, Cookie, HTTPException, Query, Request, Response, Form, \
    File, UploadFile
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# 异步
import uvicorn
# 导入了 Union 类型，用于支持多种数据类型的参数注解
from typing import Union
# Pydantic 是一个用于数据验证和序列化的 Python 模型库。
from pydantic import BaseModel, Field

import logging

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


# 请求和响应日志中间件
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # 打印请求信息
    logger.info(f"Request: {request.method} {request.url}")
    # 处理请求
    response = await call_next(request)
    # 打印响应信息
    logger.info(f"Response: {response.status_code}")
    return response


# 借助 Pydantic 来使用标准的 Python 类型声明请求体。字段的类型可以是任何有效的 Python 类型，也可以是 Pydantic 内置的类型。
class Item(BaseModel):
    id: int = None
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Blog(BaseModel):
    name: str = Field(..., title="Item Name", max_length=100)
    description: str = Field(None, title="Item Description", max_length=255)
    price: float = Field(..., title="Item Price", gt=0)


@app.get("/")
def read_root():
    # 路由处理函数返回一个字典，该字典将被 FastAPI 自动转换为 JSON 格式
    return {"Hello": "World"}


# q -- 是查询参数，指定为字符串类型或空（None）
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
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

import uuid


@app.get("/download")
async def download():
    from spider import Spider
    ss = Spider()
    img_url = ("https://assets.lummi.ai/assets/QmSGPMnVZ2wvdUNmUpf2pG4poiR3AUShaCAnxiE2DLXAUx?auto"
               "=format&w=1500")
    PATH = '/Users/jiaxiaopeng/at/'
    ss.download_picture(img_url, PATH + str(uuid.uuid1()) + '.png')
    # 使用 HTTPException 抛出异常，返回自定义的状态码和详细信息。
    ss.close()
    text = ''
    return {"status": 0, "text": text}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
