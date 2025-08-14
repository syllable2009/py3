from fastapi import FastAPI, APIRouter, HTTPException
import uvicorn
from  meili import index

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)