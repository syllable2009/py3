import asyncio

async def go():
    print("go coroutine running!")
    await asyncio.sleep(1)

async def another_coroutine():
    print("Another coroutine running!")

async def main():
    await go()  # 确保使用 await 调用 go()
    await another_coroutine()  # 同样确保使用 await 调用

# 在主程序中运行 main 函数
if __name__ == "__main__":
    asyncio.run(main())
