from playwright.sync_api import sync_playwright, Response, Download, Page, Error, expect, Browser, \
    BrowserContext

# 应该使用包含，有额外编码或者文件名称
DOWNLOAD_CONTENT_TYPES = ['application/octet-stream', 'audio/mpeg', 'lrc-application/octet-stream']
PICTURE_CONTENT_TYPES = ['image/avif', 'application/pdf', 'image/jpeg', 'image/png', 'image/gif',
                         'image/bmp', 'image/svg+xml', 'image/webp', 'image/tiff']
DOWNLOAD_CONTENT_DISPOSITION = 'attachment'

from urllib.parse import urlparse
import os


# 从url中解析文件名称
def extract_filename(url: str) -> str:
    # 解析 URL
    parsed_url = urlparse(url)
    # 获取路径部分
    path = parsed_url.path
    # 提取文件名
    filename = os.path.basename(path)
    return filename


def if_contain(lst: list, e: str) -> bool:
    if e is None:
        return False
    lower = e.lower()
    for l in lst:
        if lower in l:
            return True
    return False


# 根据content_type和content_disposition判断是否为文件下载响应
def if_download_file(content_type, content_disposition) -> bool:
    if content_type is None:
        content_type = ''
    if content_disposition is None:
        content_disposition = ''
    result = False
    if (if_contain(DOWNLOAD_CONTENT_TYPES, content_type) or if_contain(PICTURE_CONTENT_TYPES,
                                                                       content_type)
            or DOWNLOAD_CONTENT_DISPOSITION in content_disposition.lower()):
        result = True
    print(
        f"CM文件响应检测结果:{result}，content_type:{content_type}，content_disposition:"
        f"{content_disposition}")
    return result


# 根据content_type判断是否为图片响应
def if_download_picture(content_type: str) -> bool:
    if content_type is None:
        content_type = ''
    result = False
    if if_contain(PICTURE_CONTENT_TYPES, content_type):
        result = True
    print(f"CM图片响应检测结果:{result}，content_type:{content_type}")
    return result


# 利用requests开启可下载文件
import requests


def requests_download_file(url: str, path: str) -> None:
    try:
        print(f'requests开始下载: {url}')
        response = requests.get(url)
        content_type = response.headers.get('Content-Type', '""')
        content_disposition = response.headers.get('Content-Disposition', '""')
        if response.status_code == 200 and if_download_file(content_type, content_disposition):
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f'requests下载完成: {path} from {url}')
        else:
            print(f'requests下载失败，状态码或文件类型不支持下载，状态码: {response.status_code}')
    except Exception as e:
        print(f'requests下载失败，url:{url}，{e}')


# 利用wget强制开启下载文件
import wget


def wget_download_file(url: str, path: str) -> None:
    try:
        print(f'wget开始下载: {url}')
        # 下载文件
        file_name = wget.download(url, out=path)
        print(f'wget下载完成: {file_name} from {url}')
    except Exception as e:
        print(f'wget下载失败，url:{url}，{e}')


# playwright-page监听响应文件，会监听每个请求
def on_response(response: Response) -> None:
    content_disposition = response.headers.get("content-disposition", "''")
    content_type = response.headers.get("content-type", "''")
    # 监听所有响应的状态码和链接
    # print(f'Statue {response.status}: {response.url}')
    if (if_contain(DOWNLOAD_CONTENT_TYPES, content_type) and
            DOWNLOAD_CONTENT_DISPOSITION in content_disposition.lower()):
        print(f"PW on_response work，找到可下载文件，url:{response.url}，{content_type}"
              f",{content_disposition}")
        # print(response.headers)
        # print(response.request.headers)


def on_download(download: Download) -> None:
    print(
        f'PW on_download work，触发下载，url:{download.url}，file_name:{download.suggested_filename}')


class Spider:
    # 全局静态对象
    playwright = sync_playwright().start()
    # playwright.selectors.set_test_id_attribute('')
    browser: Browser = playwright.chromium.launch(headless=True, slow_mo=50)
    context: BrowserContext = browser.new_context(accept_downloads=True, ignore_https_errors=True)

    @classmethod
    def get_browser(cls) -> Browser:
        # 获取类变量的值
        return cls.browser

    @classmethod
    def get_context(cls) -> BrowserContext:
        # 获取类变量的值
        return cls.context

    @classmethod
    def get_new_page(cls) -> Page:
        # 记得关闭
        page: Page = cls.context.new_page()
        # 打开页面才能触发监听，即第一次goto无法获得
        page.on('download', lambda download: on_download(download))
        page.on('response', lambda response: on_response(response))
        # Web 中的对话框是模态框，因此会阻止进一步的页面执行，直到处理完毕
        page.on("dialog", lambda dialog: dialog.accept())
        return page

    # 记得关闭
    def open_new_page(self, url) -> Page:
        page: Page = Spider.get_new_page()
        page.goto(url, wait_until='load')
        return page

    @classmethod
    def get_page_content(cls, url, screenshot: bool = False, path: str = None) -> str:
        try:
            with Spider.get_new_page() as page:
                page.goto(url, wait_until='load')
                if screenshot and path is not None:
                    page.screenshot(path=path)
                return page.content()
        except Exception as e:
            print(f'PW 获取网页文本失败: {e}')
        finally:
            page.close()

    @classmethod
    def download_picture(cls, url: str, path: str) -> None:
        try:
            with Spider.get_new_page() as page:
                response: Response = page.goto(url, wait_until='load')
                content_type = response.headers.get("content-type", "''")
                if_image_request: bool = if_download_picture(content_type)
                if if_image_request:
                    with open(path, 'wb') as f:
                        f.write(response.body())
                    print(f"PW下载图片保存为: {path}")
                else:
                    print(f"PW非图片响应，下载操作被忽略: {url}")
        except Exception as e:
            print(f'PW下载图片失败: {e}')

    # 你不能直接下载流，因为浏览器跳转会中断，goto时报错
    def click_download_file(self, url: str, click: str, path: str) -> None:
        try:
            with Spider.get_new_page() as page:
                response: Response = page.goto(url, wait_until='load')
                with page.expect_download() as download_info:
                    # 需要在页面上检索
                    page.click(click)
                    # page.locator("a", has_text="1MB").click()
                    download = download_info.value
                # wait for download to complete
                print(f"PW即将下载文件from:{download.url}")  # 获取下载的url地址
                # 这一步只是下载下来，生成一个随机uuid值保存，代码执行完会自动清除
                print(f"PW下载临时文件to:{download.path()}")
                print(f"PW下载文件保存为:{path}")
                download.save_as(path)
        except Exception as e:
            print(f'PW下载文件失败，url:{download.url}, {e}')

    @classmethod
    def close(cls) -> None:
        if cls.browser is not None:
            cls.browser.close()
        if cls.playwright is not None:
            cls.playwright.stop()


import uuid

if __name__ == "__main__":
    spider = Spider()
    img_url = ("https://assets.lummi.ai/assets/QmSGPMnVZ2wvdUNmUpf2pG4poiR3AUShaCAnxiE2DLXAUx?auto"
               "=format&w=1500")
    PATH = '/Users/jiaxiaopeng/at/'
    spider.download_picture(img_url, PATH + str(uuid.uuid1()) + '.png')
    page_url = "https://pypi.org/project/pytest/#files"
    spider.download_picture(page_url, PATH + str(uuid.uuid1()) + '.png')
    spider.click_download_file(page_url, 'text=pytest-8.3.4.tar.gz',
                               PATH + str(uuid.uuid1()) + '.tar.gz')
    download_url = 'https://files.pythonhosted.org/packages/05/35/30e0d83068951d90a01852cb1cef56e5d8a09d20c7f511634cc2f7e0372a/pytest-8.3.4.tar.gz'
    requests_download_file(download_url, PATH + str(uuid.uuid1()) + '.tar.gz')
    wget_download_file(download_url, PATH + str(uuid.uuid1()) + '.tar.gz')
