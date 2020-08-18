
#在当前命令行运行uvicorn myapi:app --host 0.0.0.0 --port 80启动

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}