from app.base.abstract_crawler import AbstractCrawler
import app.config as config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright
from typing import Dict, List, Optional, Tuple
import os


class VOACrawler(AbstractCrawler):
    # Playwright驱动对象
    playwright: Playwright
    # chrome浏览器对象
    chrome: BrowserType
    # default上下文对象
    context: BrowserContext

    def __init__(self) -> None:
        self.index_url = "https://pypi.org/project/pytest/#files"
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def start(self):
        async with await VOACrawler.context.new_page() as page:
            response = await page.goto(self.index_url)
            print(await page.title())
            print(response.headers)

    async def init(self) -> None:
        VOACrawler.playwright = await async_playwright().start()
        VOACrawler.chromium = VOACrawler.playwright.chromium
        VOACrawler.context = await self.launch_browser(
            VOACrawler.chromium, None, self.user_agent, headless=config.HEADLESS
        )
        # stealth.min.js是一个用于防止网站被爬虫检测到的js脚本。
        current_directory = os.getcwd()
        relative_path = "libs/stealth.min.js"
        full_path = os.path.join(current_directory, relative_path)
        print(full_path)
        await VOACrawler.context.add_init_script(path=full_path)
        # 添加 cookie 属性 webId，避免网页上出现滑动验证码
        await VOACrawler.context.add_cookies(
            [
                {
                    "name": "webId",
                    "value": "xxx123",  # any value
                    "domain": ".xiaohongshu.com",
                    "path": "/",
                }
            ]
        )

    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True,
    ) -> BrowserContext:
        browser = await chromium.launch(headless=headless, proxy=playwright_proxy)  # type: ignore
        browser_context = await browser.new_context(
            viewport={"width": 1920, "height": 1080}, user_agent=user_agent
        )
        return browser_context

    @classmethod
    async def close(cls):
        await cls.context.close()
        await cls.playwright.stop()
