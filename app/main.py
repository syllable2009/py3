import asyncio
import sys
from datetime import datetime
import config
from factory import CrawlerFactory


async def main():
    print(f'-----> app start,{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    # init db
    if config.SAVE_DATA_OPTION == "db":
        # await db.init_db()
        pass
    crawler = CrawlerFactory.create_crawler(platform=config.PLATFORM)
    await crawler.init()
    await crawler.start()
    await crawler.close()
    print(f'-----> app end,{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == '__main__':

    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
        pass
    except Exception as e:
        print(e)
        sys.exit()
