import uuid
import types
from app.base.abstract_crawler import AbstractCrawler
import app.config as config
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright, Playwright, \
    expect
from typing import Dict, List, Optional, Tuple
import os
from ..pw import ChromeBrowser
from app.util import extract_filename, get_file_path, wget_download_file


class EruptCrawler(AbstractCrawler):
    chrome: ChromeBrowser

    def __init__(self) -> None:
        self.index_url = "http://jxp:8080/"
        self.domain = 'http://jxp:8080/'
        self.path = '/Users/jiaxiaopeng/at/'
        # self.user_agent = utils.get_user_agent()
        self.user_agent = config.UA if config.UA else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    async def start(self):
        async with await ChromeBrowser.get_new_page() as page:
            await page.goto(self.index_url)
            # await page.wait_for_load_state(state = 'networkidle')
            # 检查登录表单是否存在
            if_login = await page.locator('form[role="form"]').is_visible(timeout=10_000)
            print(f'{if_login}')
            if if_login is True:
                await login(page)
            # 设置语言
            # 操作
            # await page.locator('text=测试品牌').click()
            await page.locator('span[title="测试品牌"]').click()
            await add_brand(page)
            if 1 == 1:
                await page.wait_for_timeout(2_1000)
                return
            listitem_all = await page.locator(
                "xpath=//div[@class='h-min w-auto relative z-10']").all()
            # listitem_all = await (page.locator('//div[@class="list"]')
            #                       .get_by_role('listitem')
            #                       .filter(has=page.locator('.lrc'))
            #                       .all())
            print(f'共发现【{len(listitem_all)}】个资源')
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


async def login(page: Page) -> None:
    # 这里查找需要考虑页面的国际化造成的影响
    await page.locator('input[formcontrolname="userName"]').fill('erupt')
    await page.locator('input[type="password"]').fill('admin123456')
    # await page.get_by_placeholder('密码').fill('erupt')
    # page.locator('input[type="radio"][value="option1"]')
    await page.locator('button[type="submit"]').click(timeout=10_000)


async def add_brand(page: Page) -> None:
    print(f'{await page.evaluate("window.navigator.language;")}')

    # 监听对话框
    page.on('dialog', lambda dialog: {
        print('出现了弹窗：' + dialog.message())
    })

    await page.locator('text=新增 ').click()
    print(f'{page.url}')
    # print(f'{await page.content()}')
    input_all = await page.locator('xpath=//erupt-edit//erupt-edit-type//form').locator(
        'input').filter(has=page.locator('visible=true')).all()
    print(f'共发现【{len(input_all)}】个资源')

    input_all = await page.locator('xpath=//erupt-edit//erupt-edit-type//form//nz-radio-group').all()
    print(f'共发现【{len(input_all)}】个资源')
    for input in input_all:
        await input.get_by_text('是').set_checked(checked=True)
        # print(f'{await page.inner_html(input)}')
        # print(f'{await input.inner_text()}')
    #     print(f'{await page.inner_text(input)}')

    # 找到提交按钮
    await page.get_by_text("增加").locator("..").click()