import aioredis
import asyncio
from typing import Any, Optional

class RedisClient:
    def __init__(self, url: str):
        self.url = url
        self.redis = None

    async def connect(self):
        """连接到 Redis 服务器"""
        self.redis = await aioredis.from_url(self.url)

    async def close(self):
        """关闭 Redis 连接"""
        if self.redis:
            await self.redis.close()

    async def set(self, key: str, value: Any, expire: Optional[int] = None):
        """设置键值对"""
        await self.redis.set(key, value, ex=expire)

    async def get(self, key: str) -> Optional[str]:
        """获取键的值"""
        value = await self.redis.get(key)
        return value.decode("utf-8") if value else None

    async def delete(self, key: str):
        """删除键"""
        await self.redis.delete(key)

    async def exists(self, key: str) -> bool:
        """检查键是否存在"""
        return await self.redis.exists(key) > 0

    async def lpush(self, key: str, value: Any):
        """将值推入列表的左侧"""
        await self.redis.lpush(key, value)

    async def rpush(self, key: str, value: Any):
        """将值推入列表的右侧"""
        await self.redis.rpush(key, value)

    async def lrange(self, key: str, start: int = 0, end: int = -1):
        """获取列表中的所有元素"""
        values = await self.redis.lrange(key, start, end)
        return [value.decode("utf-8") for value in values]

    async def sadd(self, key: str, value: Any):
        """将值添加到集合"""
        await self.redis.sadd(key, value)

    async def smembers(self, key: str):
        """获取集合的所有成员"""
        members = await self.redis.smembers(key)
        return {member.decode("utf-8") for member in members}

# 使用示例
async def main():
    # 创建 Redis 客户端实例
    REDIS_URL = "redis://:admin1234@localhost:6379"
    redis_client = RedisClient(REDIS_URL)

    # 连接到 Redis
    await redis_client.connect()

    # 设置键值对
    await redis_client.set("my_key", "my_value")

    # 获取键值
    value = await redis_client.get("my_key")
    print(f"my_key: {value}")

    # 检查键是否存在
    exists = await redis_client.exists("my_key")
    print(f"my_key exists: {exists}")

    # 删除键
    await redis_client.delete("my_key")

    # 尝试获取已删除的键
    value = await redis_client.get("my_key")
    print(f"my_key after deletion: {value}")

    # 关闭 Redis 连接
    await redis_client.close()

# 运行示例
if __name__ == "__main__":
    asyncio.run(main())
