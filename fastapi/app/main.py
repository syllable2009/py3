from fastapi import FastAPI
import uvicorn
# 导入了 Union 类型，用于支持多种数据类型的参数注解
from typing import Union
from pydantic import BaseModel
from fastapi import Header, Cookie

app = FastAPI()

# 借助 Pydantic 来使用标准的 Python 类型声明请求体。
class Item(BaseModel):
    id: int = None
    name: str
    price: float
    is_offer: Union[bool, None] = None

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"请求:位置参数: {args},关键字参数:{kwargs}")
        print("响应:" + json.dumps(result, ensure_ascii=False, indent=4))
        return result
    return wrapper


@log
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

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)

