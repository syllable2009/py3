from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# 定义用户模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# 数据库连接信息
DATABASE_URL = "mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建所有表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据
new_user = User(name='Jane Doe', email='jane@example.com')
session.add(new_user)
session.commit()

# 查询数据
users = session.query(User).all()
for user in users:
    print(user)

# 关闭会话
session.close()
