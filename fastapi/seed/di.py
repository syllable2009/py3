from injector import Module, Injector, Binder, inject, provider, singleton
from model import Test
from testservice import TestService


# 定义依赖注入
class DatabaseModule(Module):
    def configure(self, binder: Binder) -> None:
        # binder.bind 方法用于将一个接口或抽象类与具体的实现类关联起来。这使得在请求依赖项时，injector 知道应该提供哪个具体的实现。
        binder.bind(Test, to=Test, scope=None)  # 表示每次请求都会创建一个新的实例
        binder.bind(TestService, to=TestService, scope=singleton)


injector = Injector([DatabaseModule()])


def copy(origin, target):
    index = origin._key_to_index
    for attr in dir(target):
        if not attr.startswith('_'):
            if attr in index:
                value = origin[index.get(attr)]
                if value:
                    setattr(target, attr, value)
            else:
                pass
                # print("Row does not have {}".format(attr))

if __name__ == "__main__":
    test_service = injector.get(TestService)
    # name = test_service.get_by_name('uuuuuid')
    # print("name:{}".format(name))
    # update_result = test_service.update_one(1,"8989-9090")
    # print("update_result:{}".format(update_result))
    # test_service.delete_by_aid(3)
    db = test_service.get_by_uid("11121212")
    print(type(db))
    print(db)
    dto = Test()
    # dto.uid = db.uid
    # dto.aid = db.aid
    # print(dto)
    copy(db, dto)
    print(dto)

