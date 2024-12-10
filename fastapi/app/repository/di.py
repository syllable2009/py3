# dependency injection 依赖注入容器
from sqlalchemy.orm import Session
from sqlalchemy import Engine, delete, select, update, text
from injector import Module, Injector, Binder, inject, provider, singleton
from models import User, Address, engine, new_session
from userservice import UserService


# 定义依赖注入
class DatabaseModule(Module):
    def configure(self, binder: Binder) -> None:
        # binder.bind 方法用于将一个接口或抽象类与具体的实现类关联起来。这使得在请求依赖项时，injector 知道应该提供哪个具体的实现。
        binder.bind(User, to=User, scope=None)  # 表示每次请求都会创建一个新的实例
        # session是orm的更好的封装，engine是原始的sql更灵活
        binder.bind(Session, to=new_session(), scope=None)
        binder.bind(Engine, engine, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(Address, to=Address, scope=singleton)  # 单例模式
        binder.bind(UserService, to=UserService, scope=singleton)


injector = Injector([DatabaseModule()])

if __name__ == "__main__":
    user_service = injector.get(UserService)
    print("select_by_id:{}".format(user_service.select_user_by_id(4)))
    one_engine = injector.get(Engine)
    with one_engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, name FROM users WHERE id = :id"),
            {"id": 4}
        ).fetchall()
        print("engine_get_by_id:{}".format(result))

    new_session = injector.get(Session)
    with new_session as s:
        get = s.get(User, 4)
        print(get)
    with new_session as s:
        get = s.get(User, 10)
        print(get)
