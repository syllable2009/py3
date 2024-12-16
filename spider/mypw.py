from playwright.sync_api import sync_playwright
import uuid


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     page.screenshot(path="/Users/jiaxiaopeng/pwtest.jpg")
#     browser.close()

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=50)
# page = browser.new_page()
# page.goto("https://www.baidu.com/")
# print(page.title())
# browser.close()
# playwright.stop()
def handle_download(download):
    print('download suggested_filename: {0}, path: {1}'.format(download.suggested_filename, download.path()))


PATH = '/Users/jiaxiaopeng/at/'
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=50)


def close():
    if browser is not None:
        browser.close()
    if playwright is not None:
        playwright.stop()


class Spider(object):

    @classmethod
    def get_new_page(cls):
        return browser.new_page()

    @classmethod
    def get_page_content(cls, url, screenshot=False):
        with Spider.get_new_page() as page:
            page.goto(url)
            # page.wait_for_timeout(3000);
            # page.wait_for_load_state('networkidle')
            if screenshot:
                page.screenshot(path=PATH + str(uuid.uuid1()) + '.jpg')
            return page.content()

    @classmethod
    def download_file(cls, url):
        with Spider.get_new_page() as page:
            page.goto(url)
            # page.wait_for_load_state('networkidle')
            # 定位器
            role = page.locator("a", has_text="1MB")
            print('locator result is %d' % (role.is_enabled()))
            if not role:
                return
            # 如果您不知道是什么启动了下载，您仍然可以处理该事件,需要先注册
            # page.on("download", lambda download: print(download.suggested_filename))
            page.on("download", handle_download)
            with page.expect_download() as download_info:
                # page.get_by_text("Download file").click()
                # page.get_by_role("button", name="Sign in").click()
                role.click()
            download = download_info.value
            download.save_as(PATH + download.suggested_filename)


def print_title(content: str):
    print(content)


# lxml提供etree模块，专门用来解析html和xml
from lxml import etree
def parseByXpath(content: str, xpath: str):
    if content.strip() != '':
        # 指定解析器HTMLParser会修复html缺失的信息
        parser = etree.HTMLParser(encoding="utf-8")
        # tree = etree.fromstring(content, parser=parser)
        tree = etree.HTML(content, parser=parser)
        elements = tree.xpath(xpath)
        return elements
    else:
        print('parseByXpath input is blank')
        return None


def request_page_demo():
    url = 'https://blog.51cto.com/u_16175434/8088413?articleABtest=0'
    content = Spider.get_page_content(url, screenshot=True)
    # print(content)
    # find和findall语法的xpath只能使用相对路径
    elements = parseByXpath(content, '//*[@id="markdownContent"]/p')
    if elements is None:
        pass
    else:
        print('共', len(elements), '个节点')
    for e in elements:
        if e is not None:
            # e.get('class')
            print(e.text)
            # print(e)


def down_file_demo():
    download_url = 'http://speedtest.tele2.net/'
    Spider.download_file(download_url)


if '__main__' == __name__:
    # request_page_demo()
    print('-----------------')
    # down_file_demo()
    with Spider.get_new_page() as page:
        page.goto('http://speedtest.tele2.net/')
        # page.wait_for_load_state('networkidle')
        # role可具体参考https://www.w3.org/TR/html-aria/#docconformance
        print("get_by_role: {0}".format(page.get_by_role('link', name='1MB').is_visible()))
        print("get_by_text: {0}".format(page.get_by_text('1MB').is_visible()))
        # 首层最好是用双引号
        print("locator: {0}".format(page.locator("xpath=//a[@href='1MB.zip']").is_visible()))
    close()
