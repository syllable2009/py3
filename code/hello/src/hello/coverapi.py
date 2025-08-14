from fastapi import FastAPI, APIRouter, HTTPException
import uvicorn
from meili import index
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import json
import uuid
from typing import Optional


class Item(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    url: Optional[str] = None
    price: Optional[float] = 0
    is_offer: Optional[bool] = None


router = APIRouter(tags=["封面管理"])

app = FastAPI()


@router.get("/")
@app.get("/")
def read_root():
    return {"ok"}


@router.get("/items/{item_id}")
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@router.get("/search")
@app.get("/search")
def read_item(q: str = None):
    results = index.search(q)
    hits = results.get('hits')
    return hits


@router.post("/add", response_model=Item)
@app.post("/add", response_model=Item)
def create_or_update(item: Item):
    # 字段是否为空或空字符串
    if not item.uid:
        item.uid = uuid.uuid4().hex
        index.add_documents(item.model_dump())
    else:
        index.update_documents(item.model_dump())
    print(item.model_dump())
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
