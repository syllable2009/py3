from sqlalchemy.orm import Session
from injector import Module, Injector, Binder, inject, provider, singleton
from models import User, Address, engine, new_session
from userservice import UserService





# 定义依赖注入
class DatabaseModule(Module):
    def configure(self, binder: Binder) -> None:
        # binder.bind 方法用于将一个接口或抽象类与具体的实现类关联起来。这使得在请求依赖项时，injector 知道应该提供哪个具体的实现。
        binder.bind(User, to=User, scope=None)  # 表示每次请求都会创建一个新的实例
        binder.bind(Address, to=Address, scope=singleton)  # 单例模式
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(Session, to=new_session, scope=singleton)

injector = Injector([DatabaseModule()])


if __name__ == "__main__":
    userService = injector.get(UserService)
    select_all = userService.select_all()
    print(select_all)
    # by_id = userService.select_user_by_id(4)
    # print(by_id)
    userService.create_user("lihai")






