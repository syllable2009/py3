from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright, \
    expect
from playwright._impl._api_structures import SetCookieParam, Cookie
from typing import Any, Dict, List, Literal, Optional, Sequence, TypedDict, Union
import os

# with context.expect_page() as new_page_info:
#     page.get_by_text("open new tab").click() # Opens a new tab
# new_page = new_page_info.value
def on_page(page):
    page.wait_for_load_state()
    print(f'on_page,title:{page.title()}')


# with page.expect_popup() as popup_info:
#     page.get_by_text("open the popup").click()
# popup = popup_info.value
def on_popup(popup):
    popup.wait_for_load_state()
    print(f'on_popup,title:{popup.title()}')


class ChromeBrowser:
    # Playwright驱动对象
    playwright: Playwright
    # chrome浏览器对象
    chrome: BrowserType
    # default上下文对象
    context: BrowserContext

    @classmethod
    async def get_new_page(cls) -> Page:
        page: Page = await ChromeBrowser.context.new_page()
        # page注册事件
        ChromeBrowser.context.on("page", on_page)
        page.on("popup", on_popup)
        return page

    @classmethod
    async def init(cls, playwright_proxy: Optional[Dict] = None,
                   user_agent: Optional[str] = None,
                   headless: bool = True,
                   full_path: Optional[str] = None,
                   cookies: Optional[Sequence[SetCookieParam]] = None) -> None:
        ChromeBrowser.playwright = await async_playwright().start()
        ChromeBrowser.chromium = ChromeBrowser.playwright.chromium
        ChromeBrowser.context = await cls.launch_browser(
            ChromeBrowser.chromium, None, user_agent, headless=headless
        )
        if full_path is not None:
            await ChromeBrowser.context.add_init_script(path=full_path)
        # 添加 cookie 属性 webId，避免网页上出现滑动验证码
        if cookies is not None:
            await ChromeBrowser.context.add_cookies(cookies)

    @classmethod
    async def launch_browser(
            cls,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True,
    ) -> BrowserContext:
        browser = await chromium.launch(headless=headless, proxy=playwright_proxy,
                                        slow_mo=50,
                                        channel="chrome",
                                        # 跳过反爬检测
                                        args=['--disable-blink-features=AutomationControlled']
                                        )  # type: ignore
        # viewport={"width": 1920, "height": 1080},
        browser_context = await browser.new_context(
            user_agent=user_agent, locale='zh-CN'
        )
        # 设置允许 'camera', 'microphone' 权限
        # browser_context.grant_permissions(['camera', 'microphone'])
        return browser_context

    @classmethod
    async def close(cls):
        await cls.context.close()
        await cls.playwright.stop()
