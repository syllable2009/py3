from playwright.sync_api import sync_playwright, Response, Download, Page, Error

DOWNLOAD_CONTENT_TYPE = 'application/octet-stream'
PICTURE_CONTENT_TYPES = ['image/avif']
DOWNLOAD_CONTENT_DISPOSITION = []


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
        page.goto(url, wait_until='load')
        return page

    @classmethod
    def get_page_content(cls, url, screenshot: bool = False, path: str = None):
        with Spider.get_new_page() as page:
            page.goto(url, wait_until='load')
            if screenshot and path is not None:
                page.screenshot(path=path)
            return page.content()

    @classmethod
    def download_picture(cls, url: str, path: str):
        with Spider.get_new_page() as page:
            response: Response = page.goto(url, wait_until='networkidle')
            if_image_request: bool = if_picture_request(response)
            if if_image_request:
                with open(path, 'wb') as f:
                    f.write(response.body())
                print(f"下载的文件保存为: {path}")
            else:
                print(f"非图片响应，下载操作被忽略: {url}")


    # 你不能直接下载流，因为浏览器跳转会中断，goto时报错
    def click_download_file(self, url: str, click: str, path: str):
        try:
            with Spider.get_new_page() as page:
                response: Response = page.goto(url, wait_until='networkidle')
                with page.expect_download() as download_info:
                    # 需要在页面上检索
                    page.click(click)
                    download = download_info.value
                # wait for download to complete
                print(f"即将下载文件from:{download.url}")  # 获取下载的url地址
                # 这一步只是下载下来，生成一个随机uuid值保存，代码执行完会自动清除
                print(f"下载临时文件to:{download.path()}")
                print(f"下载文件保存到:{path}")
                download.save_as(path)
        except Exception as e:
            print(f'下载失败: {e.message}')

    @classmethod
    def close(cls):
        if cls.browser is not None:
            cls.browser.close()
        if cls.playwright is not None:
            cls.playwright.stop()


def if_picture_request(response: Response):
    content_type = response.headers.get("content-type", "''")
    content_disposition = response.headers.get("content-disposition", "''")
    result = False
    if content_type in PICTURE_CONTENT_TYPES or content_disposition in DOWNLOAD_CONTENT_DISPOSITION:
        result = True
    print(f"图片响应检测结果:{result}，content_type:{content_type}，content_disposition"
          f":{content_disposition}，{response.url}")
    return result


import uuid

if __name__ == "__main__":
    spider = Spider()
    img_url = ("https://assets.lummi.ai/assets/QmSGPMnVZ2wvdUNmUpf2pG4poiR3AUShaCAnxiE2DLXAUx?auto"
               "=format&w=1500")
    PATH = '/Users/jiaxiaopeng/at/'
    # spider.download_picture(img_url, PATH + str(uuid.uuid1()) + '.png')
    page_url = "https://pypi.org/project/pytest/#files"
    file_url = "https://files.pythonhosted.org/packages/05/35/30e0d83068951d90a01852cb1cef56e5d8a09d20c7f511634cc2f7e0372a/pytest-8.3.4.tar.gz"
    spider.click_download_file(page_url,'text=pytest-8.3.4.tar.gz', PATH + str(uuid.uuid1()) + '.tar.gz')
    # page = spider.get_new_page()
