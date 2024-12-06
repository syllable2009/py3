# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import User, Base
import uvicorn

DATABASE_URL = "mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3"

# 创建数据库引擎，添加连接池配置
engine = create_engine(
    DATABASE_URL,
    pool_size=5,            # 连接池的大小
    max_overflow=10,        # 连接池外的最大连接数
    pool_timeout=30,        # 获取连接的超时时间
    pool_recycle=1800       # 每1800秒回收连接
)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建 FastAPI 应用
app = FastAPI()

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 路由：创建用户
@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}

# 路由：获取所有用户
@app.get("/users/", response_model=list)
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]

# 路由：获取特定用户
@app.get("/users/{user_id}", response_model=dict)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)