import aioredis
import asyncio

REDIS_URL = "redis://:admin1234@localhost:6379"

async def main():
    # 创建 Redis 连接
    redis = await aioredis.from_url(REDIS_URL)

    # 设置和获取键值
    await redis.set("hello", "world")
    value = await redis.get("hello")
    if value is None:
        pass
    print("hello:", value.decode("utf-8"))

    # 列表操作
    await redis.rpush("my_list", "item1")
    await redis.rpush("my_list", "item2")
    items = await redis.lrange("my_list", 0, -1)
    print("my_list:", [item.decode("utf-8") for item in items])

    # 集合操作
    await redis.sadd("my_set", "member1")
    await redis.sadd("my_set", "member2")
    members = await redis.smembers("my_set")
    print("my_set:", [member.decode("utf-8") for member in members])

    # 删除键
    delete = await redis.delete("hello")
    if delete == 0:
        pass
    value = await redis.get("hello")
    print("hello after deletion:", value)

    # 列出所有键
    keys = await redis.keys("*")
    print("All keys:", keys)

    # 检查键是否存在
    exists = await redis.exists("hello")
    print("hello exists:", exists)

    await redis.delete("my_list")
    await redis.delete("my_set")
    # 关闭 Redis 连接
    await redis.close()

# 运行异步主函数
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except ValueError as e:
        print(f"Caught an exception: {e}")
