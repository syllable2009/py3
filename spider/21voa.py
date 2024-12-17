from playwright.sync_api import expect, Locator
from spider import Spider, requests_download_file, extract_filename, wget_download_file

PATH = '/Users/jiaxiaopeng/at/'


def parse_content() -> None:
    spider = Spider()
    page = spider.get_new_page()
    url = 'https://www.21voa.com/special_english/'
    page.goto(url)
    listitem_all = (page.lrc_link('//div[@class="list"]')
                    .get_by_role('listitem')
                    .filter(has=page.get_by_role('link'))
                    .all())
    listitem_all.screenshot(path=PATH + "screenshot.png")
    print(len(listitem_all))
    for row in listitem_all:
        link = row.get_by_role('link')
        print(f"{link.first.inner_text()},{link.last.get_attribute('href')}")
    page.close()
    spider.close()


def new_page_download(locator: Locator) -> None:
    lrc_link: Locator = row_1.locator('css=.lrc')
    if lrc_link is not None:
        lrc_url = 'https://www.21voa.com' + lrc_link.first.get_attribute("href")
        filename = extract_filename(lrc_url)
        wget_download_file(lrc_url, PATH + filename)
    with page.expect_popup() as new_popup:
        locator.get_by_role('link').last.click()
    new_page = new_popup.value
    new_page.screenshot(path=PATH + "screenshot.png")
    mp3_url = new_page.locator('css=#mp3').first.get_attribute('href')
    print(f'{mp3_url},{type(mp3_url)}')
    filename = extract_filename(mp3_url)
    requests_download_file(mp3_url, PATH + filename)
    new_page.close()


if __name__ == "__main__":
    spider = Spider()
    page = spider.get_new_page()
    url = 'https://www.21voa.com/special_english/'
    page.goto(url)
    listitem_all = (page.locator('//div[@class="list"]')
                    .get_by_role('listitem')
                    # .filter(has=page.locator('.lrc'))
                    .all())
    print(len(listitem_all))
    row_1 = listitem_all[0]
    for row in listitem_all[0:4]:
        new_page_download(row)
    # print(row_1.locator('xpath=//a[@class="lrc"]').first.get_attribute('href'))
    # print(row_1.locator('css=a[class="lrc"]').first.get_attribute('href'))
    # print(row_1.locator('css=.lrc').first.get_attribute('href'))

    page.close()
    spider.close()
