from app.base.abstract_crawler import AbstractCrawler
import app.config as config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright
from typing import Dict, List, Optional, Tuple
import os
from ..pw import ChromeBrowser


class VOACrawler(AbstractCrawler):
    chrome: ChromeBrowser

    def __init__(self) -> None:
        self.index_url = "https://pypi.org/project/pytest/#files"
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def start(self):
        async with await ChromeBrowser.get_new_page() as page:
            response = await page.goto(self.index_url)
            print(await page.title())
            print(response.headers)
            await page.close()

    async def init(self) -> None:
        # stealth.min.js是一个用于防止网站被爬虫检测到的js脚本。
        current_directory = os.getcwd()
        relative_path = "libs/stealth.min.js"
        full_path = os.path.join(current_directory, relative_path)
        cookies = [
            {
                "name": "webId",
                "value": "xxx123",  # any value
                "domain": ".xiaohongshu.com",
                "path": "/",
            }
        ]
        await ChromeBrowser.init(user_agent=self.user_agent,
                                 headless=config.HEADLESS,
                                 full_path=full_path, cookies=cookies)

    async def close(cls):
        await ChromeBrowser.close()
