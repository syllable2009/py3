from fastapi import FastAPI
import uvicorn
from  meili import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/search")
def read_item(q: str = None):
    results = index.search(q)
    hits = results.get('hits')
    return hits

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)