import uuid

from app.base.abstract_crawler import AbstractCrawler
import app.config as config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright
from typing import Dict, List, Optional, Tuple
import os
from ..pw import ChromeBrowser
from app.util import extract_filename, get_file_path, wget_download_file

async def on_popup(new_page):
    print(type(new_page))
    url = await new_page.url;
    print(f'new page,url:{url}')
    await new_page.close();

class LummiCrawler(AbstractCrawler):
    chrome: ChromeBrowser

    def __init__(self) -> None:
        self.index_url = "https://www.lummi.ai/3d"
        self.domain = 'https://www.lummi.ai'
        self.path = '/Users/jiaxiaopeng/at/'
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def start(self):
        async with await ChromeBrowser.get_new_page() as page:
            await page.goto(self.index_url)

            listitem_all = await page.locator("xpath=//div[@class='h-min w-auto relative z-10']").all()
            # listitem_all = await (page.locator('//div[@class="list"]')
            #                       .get_by_role('listitem')
            #                       .filter(has=page.locator('.lrc'))
            #                       .all())
            print(f'共发现【{len(listitem_all)}】个资源')
            page.on('popup', lambda x: on_popup(x))
            for row in listitem_all[0:1]:
                href = await row.get_by_role('link').last.get_attribute("href")
                await page.goto(self.domain + href)
                print(page.url)
                async with page.expect_download() as download_info:
                    await page.get_by_text("Download", exact=True).last.click()
                download = await download_info.value
                await download.save_as(get_file_path(self.path, download.suggested_filename))
                #     lrc_url = self.domain + await row.locator('css=.lrc').first.get_attribute('href')
            #     print(f"lrc:{lrc_url}")
            #     if lrc_url is not None:
            #         filename = extract_filename(lrc_url)
            #         wget_download_file(lrc_url, self.path + filename)
            #     print(page.url)
            #
            #     a = row.get_by_role('link').last
            #     print(f'{await a.is_visible()},{await a.get_attribute("href")}')
            #     # 父级
            #     await a.locator("..").locator("..").click()
            #     print(page.url)
            #     async with page.expect_popup as new_popup:
            #         await row.get_by_role('link').first.click()
            #     new_page = await new_popup.value
            #     print(new_page.url)
                # with new_page.expect_download() as download_info:
                #     new_page.get_by_role('button').first.click()
                #     download = download_info.value
                # download.save_as(get_file_path(self.path, str(uuid.uuid1()) + ".jpeg"))
                # await new_page.screenshot(path=get_file_path(self.path, str(uuid.uuid1()) + ".png"))
            #     mp3_url = await new_page.locator('css=#mp3').first.get_attribute('href')
            #     print(f'mp3:{mp3_url}')
            #     filename = extract_filename(mp3_url)
            #     wget_download_file(mp3_url, self.path + filename)
            await page.close()

    async def init(self) -> None:
        # stealth.min.js是一个用于防止网站被爬虫检测到的js脚本。
        current_directory = os.getcwd()
        relative_path = "libs/stealth.min.js"
        full_path = os.path.join(current_directory, relative_path)
        await ChromeBrowser.init(user_agent=self.user_agent,
                                 headless=config.HEADLESS,
                                 full_path=full_path)

    async def close(cls):
        await ChromeBrowser.close()