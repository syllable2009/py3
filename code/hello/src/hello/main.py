from fastapi import FastAPI
import uvicorn
import coverapi

app = FastAPI()
app.include_router(coverapi.router, prefix="/cover")


# http://localhost:8000/docs
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)