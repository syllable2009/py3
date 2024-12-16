from playwright.sync_api import sync_playwright, Response, Download, Page
import uuid
from lxml import etree

PATH = '/Users/jiaxiaopeng/at/'
DOWNLOAD_CONTENT_TYPE = 'application/octet-stream'


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


def handle_download(response, page):
    print('download suggested_filename: {0}, path: {1}'.format(response.suggested_filename,
                                                               response.path()))
    if response.headers.get('content-type') == 'binary/octet-stream':
        # 假设我们知道文件名
        filename = "downloaded_file.bin"
        with open(filename, 'wb') as f:
            f.write(response.body())
        print(f"下载的文件保存为: {filename}")


download_content_types = ['image/avif']
download_content_disposition = []


def if_download(response: Response):
    content_type = response.headers.get("content-type", "")
    content_disposition = response.headers.get("content-disposition", "")
    print(f"if_download,content_type:{content_type},content_disposition:{content_disposition}")
    if content_type in download_content_types or content_disposition in download_content_disposition:
        return True
    return False


class Spider:
    # 全局静态对象
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=50)

    @classmethod
    def get_browser(cls):
        # 获取类变量的值
        return cls.browser

    @classmethod
    def get_new_page(cls):
        # 记得关闭
        return cls.browser.new_page(ignore_https_errors=True)

    # 记得关闭
    def open_new_page(self, url):
        page = Spider.get_new_page()
        page.goto(url)
        return page

    @classmethod
    def get_page_content(cls, url, screenshot=False):
        with Spider.get_new_page() as page:
            page.goto(url)
            # page.wait_for_timeout(3000);
            # page.wait_for_load_state('networkidle')
            if screenshot:
                page.screenshot(path=PATH + str(uuid.uuid1()) + '.png')
            return page.content()

    @classmethod
    def close(cls):
        if cls.browser is not None:
            cls.browser.close()
        if cls.playwright is not None:
            cls.playwright.stop()

    # 你不能直接下载流，因为浏览器跳转会中断，goto时报错
    @classmethod
    def download_img(cls, url, name=str(uuid.uuid1()) + ".png"):
        with Spider.get_new_page() as page:
            try:
                with page.expect_download() as download_info:
                    page.expect_event()
                    goto = page.goto(url)
                    print(download_info.value)
                    # page.on("download", lambda download: print(download.path()))

                    print(f"goto:{goto}")
                # page.wait_for_load_state("networkidle")
                # with page.expect_download() as download_info:
                #     page.locator('a[href="#pytest-8.3.4.tar.gz"]').click()
                # Perform the action that initiates download
                # download = download_info.value
                # download.save_as(PATH + download.suggested_filename)
            except Exception as e:
                print(f"Error occurred: {e}")
            # download = downlod_info.value
            # print(download.path())
            # download.save_as(PATH + download.suggested_filename)
            # print(response.all_headers())
            # print(response.headers_array())
        if 1 == 1:
            return
            download = if_download(response)
            # pic_src = page.get_attribute('//img[@id="xxx-image"]', 'src', timeout=10000)
            if not download:
                print(f"{url} 可能不是可下载的文件。")
                return
            with open(PATH + name, 'wb') as file:
                print(f"Downloading {name}...")
                file.write(response.body())

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


def download_ex_1(page):
    # 1.请求先导航到一个页面，否则没有任何效果
    # ？为什么不能直接打开下载页面：保错Page.goto: net::ERR_ABORTED。download_file_url =
    # "https://files.pythonhosted.org/packages/05/35/30e0d83068951d90a01852cb1cef56e5d8a09d20c7f511634cc2f7e0372a/pytest-8.3.4.tar.gz"
    page.goto("https://pypi.org/project/pytest/#files")
    with page.expect_download() as download_info:
        # 2.需要在页面上检索
        page.click("text=pytest-8.3.4.tar.gz")
    download = download_info.value
    # wait for download to complete
    print(f"即将下载文件from:{download.url}")  # 获取下载的url地址
    # 这一步只是下载下来，生成一个随机uuid值保存，代码执行完会自动清除
    print(f"下载临时文件to:{download.path()}")
    filename = PATH + download.suggested_filename
    print(f"下载文件保存到:{filename}")
    download.save_as(filename)


def download_ex_2(page):
    # 1.请求先导航到一个页面，否则没有任何效果
    page.goto("https://pypi.org/project/pytest/#files")
    # 用于等待页面上的下载事件，playwright下载对象会关闭
    # page.on('download', handle_download_file)
    page.on('response', lambda response: on_response(response))
    print(f"点击操作")
    page.click("text=pytest-8.3.4.tar.gz")
    print(f"完成")


# 利用requests下载文件
import requests


def requests_download_file(url: str, path: str):
    try:
        print(f'wget开始下载: {url}')
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f'下载完成: {path}')
        else:
            print(f'下载失败，状态码: {response.status_code}')
    except Exception as e:
        print(f'下载失败: {e}')


# 利用wget下载文件
import wget


def wget_download_file(url: str, path: str):
    try:
        print(f'wget开始下载: {url}')
        # 下载文件
        file_name = wget.download(url, out=path)
        print(f'下载完成: {file_name}')
    except Exception as e:
        print(f'下载失败: {e}')


def handle_download_file(download: Download):
    print(f"触发下载,即将下载文件from:{download.url}")
    print(f"{type(download)},{download.suggested_filename}")
    filename = PATH + download.suggested_filename
    wget_download_file(download.url, filename)
    # requests_download_file(download.url, filename)

def on_response(response: Response):
    content_disposition = response.headers.get("content-disposition", "")
    content_type = response.headers.get("content-type", "")
    # 监听所有响应的状态码和链接
    # print(f'Statue {response.status}: {response.url}')
    if DOWNLOAD_CONTENT_TYPE == content_type:
        print(f"on_response:{content_disposition},{content_type}")
        # 下载文件
        print(response.headers)
        print(response.request.headers)


# 安装浏览器的二进制文件
# python3 -m playwright install
import asyncio


def main(func):
    spider = Spider()
    page = spider.get_new_page()
    func(page)
    page.close()
    spider.close()


if __name__ == "__main__":
    # content = spider.get_page_content("https://blog.51cto.com/u_16175434/8088413", True)
    # 利用lxml解析html，也可以直接使用page的自带方法
    # elements = parseByXpath(content,"//*[@id='markdownContent']/p")
    # if elements is None:
    #     pass
    # else:
    #     print('共', len(elements), '个节点')
    # for e in elements:
    #     if e is not None:
    # e.get('class')
    # print(e.text)
    # print(e)
    # img_url = "https://assets.lummi.ai/assets/QmSGPMnVZ2wvdUNmUpf2pG4poiR3AUShaCAnxiE2DLXAUx?auto=format&w=1500"
    # download_file_url = "https://files.pythonhosted.org/packages/05/35/30e0d83068951d90a01852cb1cef56e5d8a09d20c7f511634cc2f7e0372a/pytest-8.3.4.tar.gz"
    # download_file_url = 'https://pypi.org/project/pytest/#files'
    main(download_ex_1)
    main(download_ex_2)
