# models.py 定义模型
from datetime import datetime
from sqlalchemy import (create_engine, text, select, update, Column, BigInteger, Integer, String,
                        func,
                        UniqueConstraint,
                        Text, DateTime)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, mapped_column, Mapped, \
    DeclarativeBase, Session
# 和 1.x API 不同，sqlalchemy2.0 API 中不再使用 query，而是使用 select 来查询数据。
from sqlalchemy import create_engine, text, select, update

DATABASE_URL = "mysql+mysqlconnector://jiaxiaopeng:admin1234@localhost/my3?charset=utf8mb4"

# 创建一个 SQLite 的内存数据库，必须加上 check_same_thread=False，否则无法在多线程中使用
engine = create_engine("sqlite:///:memory:", echo=True, future=True,
                       connect_args={"check_same_thread": False})
# 创建数据库引擎，添加连接池配置
engine = create_engine(
    DATABASE_URL,
    echo=True,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    max_overflow=10,  # 连接池外的最大连接数
    pool_timeout=30,  # 获取连接的超时时间
    pool_recycle=3600  # 每1800秒回收连接，设置时间以限制数据库自动断开
)

# 还可以使用 sessionmaker 来创建一个工厂函数，这样就不用每次都输入参数了
new_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 调用 create_all 创建所有表
# Base.metadata.create_all(engine)
# 如果只需要创建一个表
# User.__table__.create(engine)

# 定义一个数据库模型（即表结构），它允许你通过继承一个基类并定义属性来映射数据库表的列。
class Base(DeclarativeBase):
    pass

# 定义一个数据库用户orm映射类和表
class User(Base):
    __tablename__ = 'users'
    # 必须是 tuple，不能是 list，闲得慌……
    # __table_args__ = (UniqueConstraint("name", "email"),)
    # id: Mapped[int]  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id: Mapped[int] = mapped_column(BigInteger, index=True, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, unique=True)
    fullname: Mapped[str] = mapped_column(String(255), nullable=True)
    # 对于特别大的字段，还可以使用 deferred，这样默认不加载这个字段
    description: Mapped[str] = mapped_column(Text, deferred=True, nullable=True)
    # 默认值，注意传递的是函数，不是现在的时间
    create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now,
                                                  nullable=True)
    # 或者使用服务器默认值，但是必须在表创建的时候就设置好，会成为表的 schema 的一部分
    # create_time: Mapped[datetime] = mapped_column(DateTime(timezone=True),
    #                                                server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(),
                                                  default=datetime.now, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', fullname='{self.fullname}')>"

# 定义一个地址orm映射类和表
class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email_address: Mapped[str] = mapped_column(String, nullable=False)
