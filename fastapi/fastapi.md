# fastapi简化的实现流程
class FastAPI:
    def __init__(self):
        self.routes = []

    def get(self, path):
        def decorator(func):
            self.routes.append((path, func, "GET"))
            return func
        return decorator

app = FastAPI()

@app.get("/")
async def read_root():
return {"message": "Hello, World!"}

