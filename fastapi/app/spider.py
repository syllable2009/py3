import asyncio
from playwright.async_api import async_playwright, Playwright



async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=True, slow_mo=50)
    page = await browser.new_page(accept_downloads=True, ignore_https_errors=True)
    await page.goto("https://pypi.org/project/pytest/#files")
    title = await page.title()
    await page.close()
    await browser.close()
    return title

async def main():
    async with async_playwright() as playwright:
        return await run(playwright)


if __name__ == '__main__':
    # asyncio.run(main())
    print(type(main))