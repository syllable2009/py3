from selenium import webdriver

# browser = webdriver.Firefox(executable_path ="F:\GeckoDriver\geckodriver")

driver = webdriver.Chrome()
url = 'www.baidu.com'
driver.get(url)
print(driver.page_source)
driver.close