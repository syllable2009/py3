import asyncio
import config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright
from typing import Dict, List, Optional, Tuple


class DemoCrawler:
    # Playwright驱动对象
    playwright: Playwright
    # chrome浏览器对象
    chrome: BrowserType
    # default上下文对象
    context: BrowserContext

    # page: Page

    def __init__(self) -> None:
        self.index_url = "https://pypi.org/project/pytest/#files"
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def open(self):
        async with await DemoCrawler.context.new_page() as page:
            response = await page.goto(self.index_url)
            print(await page.title())
            print(response.headers)

    async def start(self) -> None:
        DemoCrawler.playwright = await async_playwright().start()
        DemoCrawler.chromium = DemoCrawler.playwright.chromium
        DemoCrawler.context = await self.launch_browser(
            DemoCrawler.chromium, None, self.user_agent, headless=config.HEADLESS
        )
        # stealth.min.js是一个用于防止网站被爬虫检测到的js脚本。
        await DemoCrawler.context.add_init_script(path="libs/stealth.min.js")
        # 添加 cookie 属性 webId，避免网页上出现滑动验证码
        await DemoCrawler.context.add_cookies(
            [
                {
                    "name": "webId",
                    "value": "xxx123",  # any value
                    "domain": ".xiaohongshu.com",
                    "path": "/",
                }
            ]
        )
        # 初始化一个页面，默认在这个页面上开始
        # DemoCrawler.page = await DemoCrawler.context.new_page()

        # async def start(self) -> None:

    #     async with async_playwright() as playwright:
    #         chromium = playwright.chromium
    #         DemoCrawler.browser_context = await self.launch_browser(
    #             chromium, None, self.user_agent, headless=config.HEADLESS
    #         )
    #         # stealth.min.js是一个用于防止网站被爬虫检测到的js脚本。
    #         await self.browser_context.add_init_script(path="libs/stealth.min.js")
    #         # 添加 cookie 属性 webId，避免网页上出现滑动验证码
    #         await self.browser_context.add_cookies(
    #             [
    #                 {
    #                     "name": "webId",
    #                     "value": "xxx123",  # any value
    #                     "domain": ".xiaohongshu.com",
    #                     "path": "/",
    #                 }
    #             ]
    #         )

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
        """Close browser context"""
        # await cls.page.close()
        # await cls.page.close()
        await cls.context.close()
        await cls.playwright.stop()


async def main():
    print('main exec')
    # crawler = CrawlerFactory.create_crawler(platform=config.PLATFORM)
    crawler = DemoCrawler()
    await crawler.start()
    await crawler.open()
    # print(crawler)
    # crawler.close()
    # await crawler.start()
    await crawler.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
