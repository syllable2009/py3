from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

def log(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())
        print(f"Calling {func.__name__}({args_str}, {kwargs_str})")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {repr(result)}")
        return result
    return wrapper

class Item(BaseModel):
    name:str
    price:float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}
@log
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == '__main__':
  uvicorn.run(app, host="127.0.0.1", port=8001)

def cache(func):
    results = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in results:
            return results[key]
        else:
            value = func(*args, **kwargs)
            results[key] = value
            return value

    return wrapper

@cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))  # 输出 55

@log
def add(a, b):
    return a + b

sum = add(3, 4)
print(sum)  # 输出 7