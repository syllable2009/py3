import uuid

from app.base.abstract_crawler import AbstractCrawler
import app.config as config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright
from typing import Dict, List, Optional, Tuple
import os
from ..pw import ChromeBrowser
from app.util import extract_filename, get_file_path, wget_download_file


class VOACrawler(AbstractCrawler):
    chrome: ChromeBrowser

    def __init__(self) -> None:
        self.index_url = "https://www.21voa.com/special_english/"
        self.domain = 'https://www.21voa.com'
        self.path = '/Users/jiaxiaopeng/at/'
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def start(self):
        async with await ChromeBrowser.get_new_page() as page:
            await page.goto(self.index_url)
            listitem_all = await (page.locator('//div[@class="list"]')
                                  .get_by_role('listitem')
                                  .filter(has=page.locator('.lrc'))
                                  .all())
            print(f'共发现【{len(listitem_all)}】个资源')
            for row in listitem_all[0:2]:
                lrc_url = self.domain + await row.locator('css=.lrc').first.get_attribute('href')
                print(f"lrc:{lrc_url}")
                if lrc_url is not None:
                    filename = extract_filename(lrc_url)
                    wget_download_file(lrc_url, self.path + filename)
                async with page.expect_popup() as new_popup:
                    await row.get_by_role('link').last.click()
                new_page = await new_popup.value
                await new_page.screenshot(path=get_file_path(self.path, str(uuid.uuid1()) + ".png"))
                mp3_url = await new_page.locator('css=#mp3').first.get_attribute('href')
                print(f'mp3:{mp3_url}')
                filename = extract_filename(mp3_url)
                wget_download_file(mp3_url, self.path + filename)
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
