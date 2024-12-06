from injector import Module, Injector, Binder, inject, provider

# 定义接口
class GreetingService:
    # @inject 应用于类的构造函数时，injector 会自动解析并提供所需的依赖项
    @inject
    def greet(self, name: str) -> str:
        pass


# 实现接口
class EnglishGreetingService(GreetingService):
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

class CnGreetingService(GreetingService):
    def greet(self, name: str) -> str:
        return f"你好, {name}!"


# 配置Injector
class AppModule(Module):

    def configure(self, binder: Binder) -> None:
        # binder.bind 方法用于将一个接口或抽象类与具体的实现类关联起来。这使得在请求依赖项时，injector 知道应该提供哪个具体的实现。
        # scope=None 表示每次请求都会创建一个新的实例
        binder.bind(GreetingService, to=EnglishGreetingService, scope=None) # 默认绑定
        binder.bind(GreetingService, to=CnGreetingService, scope=None)

    # @provider
    # def provide_greeting_service(self) -> GreetingService:
    #     return EnglishGreetingService()
    #
    # @provider
    # def provide_cn_greeting_service(self) -> GreetingService:
    #     return CnGreetingService()


# 创建Injector实例并获取依赖
injector = Injector([AppModule()])
greeting_service = injector.get(GreetingService)

# 使用依赖
print(greeting_service.greet("World"))  # 输出: Hello, World!

